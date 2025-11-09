import argparse
import os
import time
import urllib.request

import awkward as ak
import numpy as np
import plotly.graph_objects as go
import uproot
from plotly.subplots import make_subplots
from scipy.optimize import curve_fit

# Configurar argumentos
parser = argparse.ArgumentParser(
    description="Análisis de Higgs con datos ATLAS Open Data"
)
parser.add_argument("file", help="Data file URL or path to be analyzed")
parser.add_argument(
    "--cut-value",
    type=float,
    default=10000,
    help="Cut value for pT in MeV (default: 10000)",
)
parser.add_argument(
    "--min-energy",
    type=float,
    default=105,
    help="Minimum energy in GeV for fit range (default: 105)",
)
parser.add_argument(
    "--max-energy",
    type=float,
    default=160,
    help="Maximum energy in GeV for fit range (default: 160)",
)
parser.add_argument(
    "--bins", type=int, default=30, help="Number of bins for histogram (default: 30)"
)
parser.add_argument(
    "--output-dir",
    type=str,
    default="plots",
    help="Output directory for plots (default: plots)",
)
args = parser.parse_args()

# Obtener argumentos
url = args.file
cut_value = args.cut_value
min_energy = args.min_energy
max_energy = args.max_energy
n_bins = args.bins
output_dir = args.output_dir

# Validar parámetros
if min_energy >= max_energy:
    print(
        f"Error: min_energy ({min_energy}) debe ser menor que max_energy ({max_energy})"
    )
    exit(1)

filename = os.path.basename(url)
base_name = os.path.splitext(filename)[0]

print(f"\n{'=' * 60}")
print("Configuración del análisis:")
print(f"  Archivo: {filename}")
print(f"  Cut value (pT): {cut_value} MeV = {cut_value / 1000:.1f} GeV")
print(f"  Rango de energía: {min_energy} - {max_energy} GeV")
print(f"  Número de bins: {n_bins}")
print(f"  Directorio de salida: {output_dir}")
print(f"{'=' * 60}\n")

# --- 1. PREPARACIÓN Y CÁLCULO DE MASA ---

## 📦 Descarga y Apertura de Datos
if not os.path.exists(filename):
    print(f"Descargando archivo: {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print("Descarga completada.")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")
        exit(1)

start = time.time()
print(f"Abriendo archivo: {filename}")

try:
    file = uproot.open(filename)
    tree = file["mini"]
except Exception as e:
    print(f"Error al abrir el archivo ROOT: {e}")
    exit(1)

branches = tree.arrays(
    [
        "trigP",
        "photon_pt",
        "photon_eta",
        "photon_phi",
        "photon_isTightID",
        "photon_ptcone30",
        "photon_etcone20",
    ],
    library="ak",
)

## ✂️ Selección y Cortes Cinemáticos
pt = branches["photon_pt"]
eta = branches["photon_eta"]
phi = branches["photon_phi"]
tight = branches["photon_isTightID"] == 1
ptcone = branches["photon_ptcone30"]
etcone = branches["photon_etcone20"]

# Cortes de pt, eta e identificación (usando cut_value del argumento)
pt_cut = pt > cut_value
eta_abs = np.abs(eta)
eta_cut = (eta_abs < 2.37) & ((eta_abs < 1.37) | (eta_abs > 1.52))
photon_mask_no_iso = tight & pt_cut & eta_cut
good_photon_count = ak.sum(photon_mask_no_iso, axis=1)
event_mask = (good_photon_count == 2) & branches["trigP"]

# Candidatos que pasan los cortes iniciales
pt_candidates = pt[event_mask][photon_mask_no_iso[event_mask]]
eta_candidates = eta[event_mask][photon_mask_no_iso[event_mask]]
phi_candidates = phi[event_mask][photon_mask_no_iso[event_mask]]
ptcone_candidates = ptcone[event_mask][photon_mask_no_iso[event_mask]]
etcone_candidates = etcone[event_mask][photon_mask_no_iso[event_mask]]

pt1, pt2 = pt_candidates[:, 0], pt_candidates[:, 1]
ptcone1, ptcone2 = ptcone_candidates[:, 0], ptcone_candidates[:, 1]
etcone1, etcone2 = etcone_candidates[:, 0], etcone_candidates[:, 1]

# Corte de Aislamiento
iso_cond1 = (ptcone1 / pt1 < 0.065) & (etcone1 / pt1 < 0.065)
iso_cond2 = (ptcone2 / pt2 < 0.065) & (etcone2 / pt2 < 0.065)
final_event_mask = iso_cond1 & iso_cond2

pt_final = pt_candidates[final_event_mask]
eta_final = eta_candidates[final_event_mask]
phi_final = phi_candidates[final_event_mask]

## 📐 Cálculo de Masa Invariante
PT_plano = ak.to_numpy(ak.flatten(pt_final)) / 1000.0  # Convertir a GeV
ETA_plano = ak.to_numpy(ak.flatten(eta_final))
PHI_plano = ak.to_numpy(ak.flatten(phi_final))
PT1, PT2 = PT_plano[::2], PT_plano[1::2]
ETA1, ETA2 = ETA_plano[::2], ETA_plano[1::2]
PHI1, PHI2 = PHI_plano[::2], PHI_plano[1::2]
dEta = ETA1 - ETA2
dPhi = PHI1 - PHI2

mass_sq = 2 * PT1 * PT2 * (np.cosh(dEta) - np.cos(dPhi))
mass = np.sqrt(np.maximum(0, mass_sq))

end = time.time()
duration = end - start
print("\n--- Resultados de Selección y Cinemática ---")
print(
    "Tiempo de procesamiento: {} min {} s".format(
        int(duration // 60), int(duration % 60)
    )
)
print(f"Número de eventos seleccionados: {len(mass)}")
if len(mass) > 0:
    print(f"Media (M_yy): {np.mean(mass):.2f} GeV")
    print(f"Desviación estándar (M_yy): {np.std(mass):.2f} GeV")
else:
    print("¡Advertencia! No se seleccionaron eventos.")
    exit(1)

# --- 2. AJUSTE (FITTING) CON SCIPY ---


def fit_function(x, N_signal, mean, sigma, N_bkg, lambda_bkg):
    """Función de ajuste: Señal gaussiana + Fondo exponencial"""
    gauss = (
        N_signal
        * np.exp(-0.5 * ((x - mean) / sigma) ** 2)
        / (sigma * np.sqrt(2 * np.pi))
    )
    exp = N_bkg * np.exp(lambda_bkg * x)
    return gauss + exp


# Usar min_energy y max_energy de los argumentos
fit_range = [min_energy, max_energy]
counts, edges = np.histogram(mass, bins=n_bins, range=fit_range)
centers = 0.5 * (edges[:-1] + edges[1:])
bin_width = edges[1] - edges[0]
counts_density = counts / bin_width
N_events_fit = len(mass[(mass >= fit_range[0]) & (mass <= fit_range[1])])

# Parámetros iniciales y límites
p0 = [N_events_fit * 0.05, 125.0, 2.0, N_events_fit * 0.95, -0.01]
bounds = ([0, 120, 0.5, 0, -0.1], [N_events_fit * 2, 130, 5.0, N_events_fit * 2, 0])

is_valid = False
fit_results = None
fit_errors = None
popt = None

try:
    centers_np = np.asarray(centers)
    counts_density_np = np.asarray(counts_density)

    popt, pcov = curve_fit(
        fit_function, centers_np, counts_density_np, p0=p0, bounds=bounds
    )
    perr = np.sqrt(np.diag(pcov))

    fit_results = {
        "N_signal": popt[0] * bin_width,
        "mean": popt[1],
        "sigma": popt[2],
        "N_bkg": popt[3] * bin_width,
        "lambda_bkg": popt[4],
    }
    fit_errors = {
        "N_signal": perr[0] * bin_width,
        "mean": perr[1],
        "sigma": perr[2],
        "N_bkg": perr[3] * bin_width,
        "lambda_bkg": perr[4],
    }

    print("\n--- Resultados del Ajuste ---")
    print(
        f"Masa del Higgs (Media): {fit_results['mean']:.3f} ± {fit_errors['mean']:.3f} GeV"
    )
    print(
        f"Ancho de la Señal (Sigma): {fit_results['sigma']:.3f} ± {fit_errors['sigma']:.3f} GeV"
    )
    print(
        f"N_Signal (Gaussiana): {fit_results['N_signal']:.1f} ± {fit_errors['N_signal']:.1f}"
    )
    print(
        f"N_Background (Exponencial): {fit_results['N_bkg']:.1f} ± {fit_errors['N_bkg']:.1f}"
    )

    is_valid = True

except RuntimeError as e:
    print(f"\n--- ¡ADVERTENCIA! El ajuste no convergió: {e}")
except Exception as e:
    print(f"\n--- Error en el ajuste: {e}")

# --- 3. GRÁFICO FINAL CON PLOTLY ---

os.makedirs(output_dir, exist_ok=True)
fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=(
        f"Vista General ({min_energy}–{max_energy} GeV, Log Scale)",
        "Zoom y Componentes (120–135 GeV)",
    ),
    horizontal_spacing=0.12,
)

# ---------------------------------------------
# Panel Izquierdo: Vista General
# ---------------------------------------------
fig.add_trace(
    go.Bar(
        x=centers,
        y=counts,
        name="Datos",
        marker_color="black",
        opacity=0.6,
        error_y=dict(type="data", array=np.sqrt(counts), visible=True),
    ),
    row=1,
    col=1,
)

if is_valid:
    x_fit = np.linspace(fit_range[0], fit_range[1], 200)
    y_fit = fit_function(x_fit, *popt) * bin_width

    fig.add_trace(
        go.Scatter(
            x=x_fit,
            y=y_fit,
            mode="lines",
            name="Fit Total",
            line=dict(color="red", width=3),
        ),
        row=1,
        col=1,
    )

fig.update_yaxes(type="log", row=1, col=1, title_text="Events / Bin (Log Scale)")
fig.update_xaxes(
    title_text="Invariant Mass m\u03b3\u03b3 (GeV)", range=fit_range, row=1, col=1
)

# Anotación con resultados
if is_valid:
    annotation_text = (
        f"Entries: {len(mass)}<br>"
        f"Cut (pT): {cut_value / 1000:.1f} GeV<br>"
        f"M_H: {fit_results['mean']:.3f} ± {fit_errors['mean']:.3f} GeV<br>"
        f"σ: {fit_results['sigma']:.3f} ± {fit_errors['sigma']:.3f} GeV"
    )

    fig.add_annotation(
        text=annotation_text,
        xref="x domain",
        yref="y domain",
        x=0.72,
        y=0.85,
        showarrow=False,
        font=dict(size=11, color="black"),
        bgcolor="rgba(255, 255, 255, 0.85)",
        bordercolor="black",
        borderwidth=1,
        row=1,
        col=1,
    )

# ---------------------------------------------
# Panel Derecho: Zoom
# ---------------------------------------------
zoom_range_fit = [120, 135]
bins_zoom = 20
counts_zoom, edges_zoom = np.histogram(mass, bins=bins_zoom, range=zoom_range_fit)
centers_zoom = np.asarray(0.5 * (edges_zoom[:-1] + edges_zoom[1:]))
bin_width_zoom = edges_zoom[1] - edges_zoom[0]

fig.add_trace(
    go.Bar(
        x=centers_zoom,
        y=counts_zoom,
        name="Datos (Zoom)",
        marker_color="black",
        opacity=0.6,
        showlegend=False,
        error_y=dict(type="data", array=np.sqrt(counts_zoom), visible=True),
    ),
    row=1,
    col=2,
)

if is_valid:
    x_fit_zoom = np.linspace(zoom_range_fit[0], zoom_range_fit[1], 200)

    y_fit_zoom = fit_function(x_fit_zoom, *popt) * bin_width_zoom
    gauss_only_params = [popt[0], popt[1], popt[2], 0, 0]
    y_signal = fit_function(x_fit_zoom, *gauss_only_params) * bin_width_zoom
    bkg_only_params = [0, 0, 1, popt[3], popt[4]]
    y_bkg = fit_function(x_fit_zoom, *bkg_only_params) * bin_width_zoom

    fig.add_trace(
        go.Scatter(
            x=x_fit_zoom,
            y=y_fit_zoom,
            mode="lines",
            name="Fit Total",
            line=dict(color="red", width=3),
        ),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Scatter(
            x=x_fit_zoom,
            y=y_signal,
            mode="lines",
            name="Señal (Gauss)",
            line=dict(color="blue", dash="dash", width=2.5),
        ),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Scatter(
            x=x_fit_zoom,
            y=y_bkg,
            mode="lines",
            name="Fondo (Exp)",
            line=dict(color="green", dash="dot", width=2),
        ),
        row=1,
        col=2,
    )

fig.update_xaxes(
    title_text="Invariant Mass m\u03b3\u03b3 (GeV)", range=zoom_range_fit, row=1, col=2
)
fig.update_yaxes(title_text="Events / Bin", row=1, col=2)

# Configuración general del layout
fig.update_layout(
    title_text=f"Análisis {base_name} - Cut:{cut_value / 1000:.1f}GeV, E:[{min_energy}-{max_energy}]GeV",
    height=600,
    showlegend=True,
    legend_title="Componentes",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    template="plotly_white",
)

# Nombre de archivo con todos los parámetros
output_filename = f"plotly_higgs_{base_name}_cut{int(cut_value)}_E{int(min_energy)}-{int(max_energy)}.html"
output_path = os.path.join(output_dir, output_filename)
fig.write_html(output_path)

print(f"\n{'=' * 60}")
print("✅ ¡Análisis completado exitosamente!")
print(f"📊 Gráfico guardado en: {output_path}")
print(f"{'=' * 60}\n")
