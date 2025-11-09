# ⚛️ El Físico Robot (Physics on Autopilot)

[![GitHub Actions | Quarto Publish](https://img.shields.io/github/actions/workflow/status/Analisis-de-Gatos/robot-physicist/publish-site.yml?label=GitHub%20Actions&style=for-the-badge&logo=github)](https://github.com/Analisis-de-Gatos/robot-physicist/actions?query=workflow%3A%22Quarto+Publish%22)
[![GitHub Pages Status](https://img.shields.io/badge/Resultados-En%20Línea-blue)](https://analisis-de-gatos.github.io/robot-physicist/)
[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

**Retador:** Arturo Sánchez | **Hackers:** [![Equipo Gatos](https://img.shields.io/badge/Equipo-An%C3%A1lisis_de_Gatos-001855?style=plastic&)](#integrantes)

---

## 🌟 Resumen del Proyecto

Un *pipeline* CI/CD para análisis de datos abiertos de ATLAS (CERN), integrando Python, marimo y Quarto para reproducibilidad y ciencia transparente.  
Con cada `git push` a `main`, se desencadena todo el proceso: configuración, instalación de librerías, análisis físico, compilación del sitio y publicación automática.

### 🔗 Resultados en Vivo

> Puedes explorar el informe actualizado y los gráficos interactivos aquí:  
> **[Ver el Sitio Web Publicado](https://analisis-de-gatos.github.io/robot-physicist/)**

---

## ⚙️ Tecnologías Principales

| Característica       | Herramientas/Frameworks           | Propósito                                   |
| :------------------- | :------------------------------- | :------------------------------------------ |
| Análisis Físico      | Python, uproot, awkward, hist     | Leer datos ROOT y análisis de física        |
| Interactividad       | marimo                           | Widgets y celdas reactivas en la web        |
| Sitio Web            | Quarto                           | Sitio web profesional/documentación         |
| Automatización CI/CD | GitHub Actions                   | Orquestación de todo el flujo automatizado  |

---

## 📁 Estructura del Repositorio

```
.
├── .github/workflows/
│   └── publish-site.yml        # CI/CD: Workflow principal (compila y publica el sitio)
├── robot-physicist-website/   # Sitio Quarto con análisis y páginas web
│   ├── _extensions/marimo-team/marimo # Extensión marimo para Quarto
│   │    ├── _extension.yml     # Configuración de la extensión
│   │    ├── command.py         # EJecuta comandos marimo
│   │    ├── extract.py         # Extrae celdas o datos
│   │    ├── marimo-execute.lua # Ejecuta marimo en Quarto
│   │    └── utils.lua          # Funciones de utilidad
│   ├── charts/                 # Subpáginas/módulos de análisis
│   │    ├── marimotest copy/   # Experimentos o tests
│   │    │    └── index.qmd     # Test documentado
│   │    ├── marimotest/
│   │    │    └── index.qmd     # Análisis experimental
│   │    └── index.qmd          # Índice de charts
│   ├── .gitignore              # Excluir archivos temporales/locales
│   ├── _quarto.yml             # Configuración global Quarto
│   ├── about.qmd               # Sobre el proyecto/equipo
│   ├── fondo.jpg               # Imagen visual opcional
│   ├── index.qmd               # Página principal
│   ├── main.py                 # Script principal de análisis
│   └── styles.css              # Personalización visual
├── .gitignore                  # Ignorar archivos globales
├── requirements.txt            # Dependencias Python
├── LICENSE                     # Licencia MIT
└── README.md                   # Documentación principal
```

---

## 💻 Desarrollo Local

### 1. Requisitos

- Python 3.9 o superior
- [Quarto](https://quarto.org/docs/get-started/)

### 2. Instalación y Ejecución

```
git clone https://github.com/Analisis-de-Gatos/robot-physicist.git
cd robot-physicist
pip install -r requirements.txt
cd robot-physicist-website
quarto preview
```

---

## 🤝 Cómo Contribuir

- Lee los comentarios y/o README en cada carpeta para buenas prácticas y requisitos.
- Para nuevos análisis:
  - Crea subcarpetas en `charts/` con un `index.qmd` y documentación breve.
  - Usa comentarios para explicar objetivos y lógica.
  - Si tu análisis es interactivo, implementa bloques marimo.
- Scripts y utilidades se agregan en la extensión marimo o en `main.py`.

---

## 🤖 CI/CD Automatizado

El archivo `.github/workflows/publish-site.yml` maneja la automatización completa:

* **Flujo:** `push` ➡️ Configuración del entorno ➡️ Instalación de `uproot`/`marimo` ➡️ **`quarto render`** (ejecuta el análisis) ➡️ Despliegue a GitHub Pages.

Este *pipeline* garantiza que el sitio web refleje siempre el **resultado más reciente y reproducible** de tu análisis científico.

---

## 📚 Recursos

* **CERN Open Data:** Datasets de 13 TeV del experimento ATLAS [https://opendata.cern.ch/record/12360].
* **Integración marimo + Quarto:** [https://github.com/marimo-team/quarto-marimo](https://github.com/marimo-team/quarto-marimo)
* **Guía de marimo:** [https://docs.marimo.io/](https://docs.marimo.io/)

MIT 2025 — ver [`LICENSE`](./LICENSE) para detalles.

---

## Integrantes

[![Angel](https://img.shields.io/badge/Angel-008000?style=flat-square&logo=github)](https://github.com/aangcontreras)
[![Antonia](https://img.shields.io/badge/Antonia-pink?style=flat-square&logo=github)](https://github.com/AntoniaMGI)
[![Eugenia](https://img.shields.io/badge/Eugenia-241571?style=flat-square&logo=github)](https://github.com/eunight)
[![Juan Carlos](https://img.shields.io/badge/Juan%20Carlos-6a1b9a?style=flat-square&logo=github)](https://github.com/Jcosmic)
[![Juan Daniel](https://img.shields.io/badge/Juan%20Daniel-0288d1?style=flat-square&logo=github)](https://github.com/Vzkey0)

---

2025.
