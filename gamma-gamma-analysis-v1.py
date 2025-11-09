import argparse
import os
import time

import ROOT
from ROOT import TMath

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Data file to be analyzed")
parser.add_argument(
    "--cut-value", type=list, default=10000, help="Cut value for the analysis"
)
parser.add_argument(
    "--min-energy", type=list, default=105, help="Minimum energy in GeV"
)
parser.add_argument(
    "--max-energy", type=list, default=160, help="Maximum energy in GeV"
)

args = parser.parse_args()

# Get the arguments
root_file_url = args.file
cut_value = args.cut_value
min_energy = args.min_energy
max_energy = args.max_energy

for cut_value in cut_value:
    for min_energy in min_energy:
        for max_energy in max_energy:
            if min_energy < max_energy:

print("Analyzing with parameters:")
print(f"- Cut value: {cut_value}")
print(f"- Energy range: {min_energy} - {max_energy} GeV")

start = time.time()

# Open the ROOT file from the provided URL
f = ROOT.TFile.Open(root_file_url)
canvas = ROOT.TCanvas("Canvas", "cz", 800, 600)

tree = f.Get("mini")
tree.GetEntries()

# Invariant mass histogram definition
hist = ROOT.TH1F(
    "h_M_Hyy",
    "Diphoton invariant-mass ; Invariant Mass m_{yy} [GeV] ; events",
    30,
    min_energy,
    max_energy,
)

Photon_1 = ROOT.TLorentzVector()
Photon_2 = ROOT.TLorentzVector()
n = 0

for event in tree:
    n += 1
    # Print progress for every 10,000 events
    if n % cut_value == 0:
        print(n)

    # Trigger condition
    if tree.trigP:
        goodphoton_index = [0] * 5
        goodphoton_n = 0
        photon_index = 0

        # Loop over photons in the event
        for j in range(tree.photon_n):
            if (
                tree.photon_isTightID[j]
                and tree.photon_pt[j] > cut_value
                and (TMath.Abs(tree.photon_eta[j]) < 2.37)
                and (
                    TMath.Abs(tree.photon_eta[j]) < 1.37
                    or TMath.Abs(tree.photon_eta[j]) > 1.52
                )
            ):
                goodphoton_n += 1
                goodphoton_index[photon_index] = j
                photon_index += 1

        # Process only if there are exactly two good photons
        if goodphoton_n == 2:
            goodphoton1_index = goodphoton_index[0]
            goodphoton2_index = goodphoton_index[1]

            # Isolation conditions with configurable cut value
            if (
                (
                    tree.photon_ptcone30[goodphoton1_index]
                    / tree.photon_pt[goodphoton1_index]
                    < cut_value
                )
                and (
                    tree.photon_etcone20[goodphoton1_index]
                    / tree.photon_pt[goodphoton1_index]
                    < cut_value
                )
                and (
                    tree.photon_ptcone30[goodphoton2_index]
                    / tree.photon_pt[goodphoton2_index]
                    < cut_value
                )
                and (
                    tree.photon_etcone20[goodphoton2_index]
                    / tree.photon_pt[goodphoton2_index]
                    < cut_value
                )
            ):
                Photon_1.SetPtEtaPhiE(
                    tree.photon_pt[goodphoton1_index] / 1000.0,
                    tree.photon_eta[goodphoton1_index],
                    tree.photon_phi[goodphoton1_index],
                    tree.photon_E[goodphoton1_index] / 1000.0,
                )
                Photon_2.SetPtEtaPhiE(
                    tree.photon_pt[goodphoton2_index] / 1000.0,
                    tree.photon_eta[goodphoton2_index],
                    tree.photon_phi[goodphoton2_index],
                    tree.photon_E[goodphoton2_index] / 1000.0,
                )

                Photon_12 = Photon_1 + Photon_2
                mass = Photon_12.M()
                # Apply energy range cuts
                if min_energy <= mass <= max_energy:
                    hist.Fill(mass)

# Draw and save the histogram
os.makedirs("plots", exist_ok=True)
base_name = os.path.basename(root_file_url).replace(".root", "")
params_suffix = f"_cut{cut_value}_E{min_energy}-{max_energy}"
output_png = f"plots/histogram_{base_name}{params_suffix}.png"
output_root = f"plots/histogram_{base_name}{params_suffix}.root"
hist.Draw("E")
canvas.SetLogy()
canvas.SaveAs(output_png)

# Save histogram in .root format
root_output_file = ROOT.TFile(output_root, "RECREATE")
hist.Write()
root_output_file.Close()

end = time.time()
duration = end - start
print("Finished in {} min {} s".format(int(duration // 60), int(duration % 60)))
