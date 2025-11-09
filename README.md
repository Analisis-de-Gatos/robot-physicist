# ⚛️ El Físico Robot (Physics on Autopilot)


[![GitHub Actions | Quarto Publish](https://img.shields.io/github/actions/workflow/status/Analisis-de-Gatos/robot-physicist/publish-site.yml?label=GitHub%20Actions&style=for-the-badge&logo=github)](https://github.com/Analisis-de-Gatos/robot-physicist/actions?query=workflow%3A%22Quarto+Publish%22)
[![GitHub Pages Status](https://img.shields.io/badge/Resultados-En%20Línea-blue)](https://analisis-de-gatos.github.io/robot-physicist/)
[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE) [![Licencia: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

**Retador:** Arturo Sánchez | **Institución:** inait SA | **Hackers:** [![Equipo Gatos](https://img.shields.io/badge/Equipo-An%C3%A1lisis_de_Gatos-001855?style=plastic&)](#integrantes)

---

## 🌟 Resumen del Proyecto

Un *pipeline* CI/CD para análisis de datos abiertos de ATLAS (CERN), integrando Python, Quarto y dependencias modernas para reproducibilidad y ciencia transparente.  
Con cada `git push` a `main`, se ejecuta todo el proceso: configuración, análisis físico, compilación del sitio y publicación automática.

### 🔗 Resultados en Vivo

> Puedes explorar el informe actualizado y los gráficos interactivos aquí:  
> **[Ver el Sitio Web Publicado](https://analisis-de-gatos.github.io/robot-physicist/)**

---

## ⚙️ Tecnologías Principales

| Característica       | Herramientas/Frameworks     | Propósito                                   |
| :------------------- | :------------------------- | :-------------------------------------------|
| Análisis Físico      | Python, uproot, awkward, hist, Plotly | Lectura, exploración y visualización física |
| Sitio Web            | Quarto                     | Documentación reproducible y visual         |
| Dependencias         | uv, pyproject.toml         | Entornos reproducibles y modernos           |
| Automatización CI/CD | GitHub Actions             | Orquestación y despliegue                   |

---

## 📁 Estructura del Repositorio

```
.
├── .github/
│   └── workflows/
│       ├── publish-site.yml                   # CI/CD: Flujo para construir y desplegar el sitio Quarto.
│       └── workflow-plotly-higgs-analysis.yml # CI/CD: Flujo para ejecutar el script de análisis.
├── data_analysis/                             # Contiene scripts y datos del análisis.
│   ├── data.csv                               # Fuente de datos para el análisis.
│   ├── plotly_higgs_analysis.py               # Script principal de Python para generar gráficos Plotly.
│   └── plots/                                 # Directorio de plots intermedios.
├── robot-physicist-website/                   # Archivos fuente para la construcción del sitio web Quarto.
│   ├── .gitignore
│   ├── .python-version
│   ├── _quarto.yml                            # Configuración global de Quarto.
│   ├── about.qmd                              # Fuente de la página "Acerca de".
│   ├── index.qmd                              # Fuente de la página principal.
│   ├── main.py                                # Script principal (utilidad o punto de entrada).
│   ├── pyproject.toml                         # Configuración y dependencias de Python.
│   ├── uv.lock                                # Archivo de bloqueo de dependencias.
│   ├── styles.css
│   └── logo.png
├── atlas-dataset-A/                           # Resultados y documentación del análisis del Dataset A.
│   ├── histogramas/                           # Contiene histogramas (.png, .root).
│   ├── plots/                                 # Contiene gráficos interactivos HTML generados (plotly_higgs_data_A...).
│   └── index.qmd                              # Documento Quarto para el análisis del Dataset A.
├── atlas-dataset-B/                           # Análisis específico para el Dataset B.
├── atlas-dataset-C/                           # Análisis específico para el Dataset C.
├── atlas-dataset-D/                           # Análisis específico para el Dataset D.
├── LICENSE
└── README.md
```

---

## 🤖 Automatización Total vía GitHub Actions

Toda la integración y despliegue continuo está contenida en **un solo workflow** `.github/workflows/publish-site.yml`, que ejecuta todos los pasos necesarios de análisis y publicación del sitio web automáticamente o bajo demanda:

- **Automático:**  
  Cada vez que se hace `push` a la rama `main`, el pipeline se ejecuta sin intervención del usuario.
- **Manual, desde interfaz:**  
  Puedes forzar la ejecución del pipeline y el despliegue usando el botón “Run workflow” en la pestaña **Actions** → "Quarto Publish (Físico Robot CI/CD)", sin editar ni ver el código del workflow.

**No necesitas modificar ningún archivo de GitHub Actions.**  
Sólo haz cambios en tu código o documentación; la automatización CI/CD se encarga del resto.

> Si haces un fork, podrás lanzar el proceso tú mismo desde la pestaña **Actions** en tu repositorio. 
> Los permisos requeridos son los de cualquier flujo GitHub Pages estándar.

---

## 💻 Desarrollo Local

### 1. Requisitos

- Python 3.9 o superior
- [Quarto](https://quarto.org/docs/get-started/)
- [uv](https://github.com/astral-sh/uv) (opcional, pero recomendado para manejo de dependencias reproducible)

### 2. Instalación y Ejecución

```
git clone https://github.com/Analisis-de-Gatos/robot-physicist.git
cd robot-physicist
cd robot-physicist-website
uv pip install -r pyproject.toml   # O utiliza pip install -r requirements.txt si solo tienes ese archivo
quarto preview
```

---

## 🤝 Cómo Colaborar o Agregar Análisis

### Para proponer cambios generales:
Haz un fork del repositorio, crea tu propia rama y abre un Pull Request (PR).

### Para agregar un nuevo análisis:
- Crea una carpeta para tu dataset/análisis (por ejemplo, `atlas-dataset-E`).
- Añade los scripts y datos en la carpeta correspondiente de `data_analysis` si se requieren nuevos análisis.
- Agrega un archivo `index.qmd` en la carpeta específica, documentando objetivos y métodos.
- Si tu análisis es interactivo, implementa bloques marimo dentro del `.qmd`.
- Si introduces módulos, scripts o dependencias nuevos, actualiza el `pyproject.toml` y el README correspondiente.

### Para scripts o utilidades generales:
Puedes contribuirlos en el workspace de análisis o la web (`robot-physicist-website/`) y documentar su uso.

> Sugerencia: Lee los comentarios y/o README de cada carpeta antes de contribuir, para mantener buenas prácticas y coherencia en el repositorio.

---

## 📚 Recursos

- **CERN Open Data:** Datasets de 13 TeV del experimento ATLAS [https://opendata.cern.ch/record/12360].
- **Quarto:** [https://quarto.org/](https://quarto.org/)
- **Plotly:** [https://plotly.com/python/](https://plotly.com/python/)
- **uv (gestión de dependencias):** [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

---

## 📝 Licencia

Este proyecto —incluyendo el video de YouTube y todos los materiales audiovisuales— está protegido por:

MIT 2025 — ver [`LICENSE`](./LICENSE) para detalles.

🔓 **Creative Commons Attribution 4.0 Internacional (CC BY 4.0)**

Puedes compartir, copiar, remezclar, adaptar y transformar el contenido para cualquier propósito, incluso comercial, siempre que otorgues crédito a los autores.  
Más información 👉 [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

✨ ¡La ciencia abierta es para todos!

---

## Integrantes

[![Angel](https://img.shields.io/badge/Angel-008000?style=flat-square&logo=github)](https://github.com/aangcontreras) [![Antonia](https://img.shields.io/badge/Antonia-FF69B4?style=flat-square&logo=github)](https://github.com/AntoniaMGI) [![Eugenia](https://img.shields.io/badge/Eugenia-241571?style=flat-square&logo=github)](https://github.com/eunight) [![Juan Carlos](https://img.shields.io/badge/Juan%20Carlos-6a1b9a?style=flat-square&logo=github)](https://github.com/Jcosmic) [![Juan Daniel](https://img.shields.io/badge/Juan%20Daniel-0288d1?style=flat-square&logo=github)](https://github.com/Vzkey0)

---

2025.
