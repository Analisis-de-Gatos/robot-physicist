# ⚛️ El Físico Remoto (Physics on Autopilot)

[![GitHub Actions | Quarto Publish](https://img.shields.io/github/actions/workflow/status/Analisis-de-Gatos/robot-physicist/publish-site.yml?label=GitHub%20Actions&style=for-the-badge&logo=github)](https://github.com/Analisis-de-Gatos/robot-physicist/actions?query=workflow%3A%22Quarto+Publish%22)
[![GitHub Pages Status](https://img.shields.io/badge/Resultados-En%20Línea-blue)](https://analisis-de-gatos.github.io/robot-physicist/)
[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

**Retador:** Arturo Sánchez | **Hackers:** [![Equipo Gatos](https://img.shields.io/badge/Equipo-An%C3%A1lisis_de_Gatos-001855?style=plastic&)](#integrantes)

---

## 🌟 Resumen del Proyecto: Ciencia Transparente y Automatizada

Este proyecto implementa un *pipeline* **CI/CD (Integración y Despliegue Continuo)** para el análisis de **datos abiertos del experimento ATLAS (CERN)**, utilizando **Python, marimo y Quarto**. El objetivo es lograr la **máxima reproducibilidad y transparencia científica**. 

Cada `git push` a la rama principal desencadena una GitHub Action que ejecuta el siguiente flujo:

1.  **Configura** el entorno Python y Quarto.
2.  **Instala** las dependencias de física (`uproot`, `awkward-array`, etc.).
3.  **Ejecuta** el análisis físico con Python y **marimo**.
4.  **Compila** el sitio web profesional con **Quarto** (`quarto render`).
5.  **Publica** el sitio web completo en **GitHub Pages**.

### 🔗 Resultados en Vivo

El informe y los gráficos interactivos generados por la última ejecución automatizada (CI) están disponibles públicamente:

➡️ **[Ver el Sitio Web Publicado (Actualizado Automáticamente)](https://analisis-de-gatos.github.io/robot-physicist/)**

---

## ⚙️ Tecnologías y Características Clave

| Característica | Herramientas | Propósito en el Reto |
| :--- | :--- | :--- |
| **Análisis Físico** | Python, `uproot`, `awkward-array`, `hist` | Lectura eficiente del formato **ROOT** y cálculo de masas invariantes. |
| **Interactividad** | **marimo** | Permite construir celdas reactivas y *widgets* para un análisis dinámico en la web. |
| **Documentación** | **Quarto** | Generación del sitio web profesional y la integración del contenido dinámico de marimo. |
| **Automatización (CI/CD)** | **GitHub Actions** | Orquestación del flujo completo: análisis, renderizado y despliegue continuo. |

---

## 📁 Estructura del Repositorio

```

.
.
├── .github/workflows/
│   └── publish-site.yml        # CI/CD: construye y publica el sitio automáticamente
├── robot-physicist-website/   # Contiene todo el sitio Quarto y análisis
│   ├── _extensions/marimo-team/marimo # Extensión marimo para Quarto
│   │    ├── _extension.yml     # Configuración de la extensión
│   │    ├── command.py         # Ejecuta comandos marimo
│   │    ├── extract.py         # Extrae celdas o datos
│   │    ├── marimo-execute.lua # Ejecución reactiva de marimo
│   │    └── utils.lua          # Utilidades para la extensión
│   ├── charts/                 # Subpáginas y módulos de análisis
│   │    ├── marimotest copy/   # Experimentos o tests (agrega README)
│   │    │    └── index.qmd     # Explica el test al inicio del archivo
│   │    ├── marimotest/
│   │    │    └── index.qmd     # Análisis experimental con marimo
│   │    └── index.qmd          # Índice de la sección charts
│   ├── .gitignore              # Ignora archivos temporales/locales
│   ├── _quarto.yml             # Configuración global del sitio Quarto
│   ├── about.qmd               # Página "Sobre el proyecto/equipo"
│   ├── fondo.jpg               # Imagen de fondo (opcional)
│   ├── index.qmd               # Página principal del sitio
│   ├── main.py                 # Script principal para rutinas científicas
│   └── styles.css              # Personalización visual del sitio
├── .gitignore                  # Ignora archivos temporales generales
├── requirements.txt            # Dependencias Python del análisis
├── LICENSE                     # Licencia del repositorio
└── README.md                   # Documentación principal y guía de uso


````
---

## 💻 Desarrollo Local

Para desarrollar el análisis y previsualizar el sitio web en tu máquina local:

### 1. Requisitos Previos

1.  **Instalar Python (3.9+).**
2.  **Instalar Quarto:** Sigue las instrucciones oficiales de instalación.

    ➡️ [https://quarto.org/docs/get-started/](https://quarto.org/docs/get-started/)
    
### 2. Configuración y Ejecución

1. **Clona el repositorio y navega al directorio raíz:**
   ```
   git clone https://github.com/Analisis-de-Gatos/robot-physicist.git
   cd robot-physicist
   ```
2. **Instala dependencias:**
   ```
   pip install -r requirements.txt
   ```
3. **Lanza el sitio web localmente:**
   ```
   cd robot-physicist-website
   quarto preview
   ```
---

## 🤖 Automatización y CI/CD (GitHub Actions)

El archivo `.github/workflows/publish-site.yml` maneja la automatización completa:

* **Flujo:** `push` ➡️ Configuración del entorno ➡️ Instalación de `uproot`/`marimo` ➡️ **`quarto render`** (ejecuta el análisis) ➡️ Despliegue a GitHub Pages.

Este *pipeline* garantiza que el sitio web refleje siempre el **resultado más reciente y reproducible** de tu análisis científico.

---

## 📚 Recursos y Licencia

* **CERN Open Data:** Datasets de 13 TeV del experimento ATLAS [https://opendata.cern.ch/record/12360].
* **Integración marimo + Quarto:** [https://github.com/marimo-team/quarto-marimo](https://github.com/marimo-team/quarto-marimo)
* **Guía de marimo:** [https://docs.marimo.io/](https://docs.marimo.io/)

Este repositorio está publicado bajo la licencia **MIT**. Consulta el archivo [`./LICENSE`](./LICENSE) para detalles completos.

## Integrantes

[![Angel](https://img.shields.io/badge/Angel-008000?style=flat-square&logo=github)](enlace-perfil)
[![Antonia](https://img.shields.io/badge/Antonia-pink?style=flat-square&logo=github)](enlace-perfil) 
[![Eugenia](https://img.shields.io/badge/Eugenia-241571?style=flat-square&logo=github)](enlace-perfil)
[![Juan Carlos](https://img.shields.io/badge/Juan%20Carlos-6a1b9a?style=flat-square&logo=github)](enlace-perfil)
[![Juan Daniel](https://img.shields.io/badge/Juan%20Daniel-0288d1?style=flat-square&logo=github)](enlace-perfil)
