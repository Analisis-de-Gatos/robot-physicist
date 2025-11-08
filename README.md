# ⚛️ El Físico Remoto (Physics on Autopilot)

[![GitHub Actions Status](https://github.com/tu-usuario/tu-repositorio/workflows/Quarto%20Publish/badge.svg)](https://github.com/tu-usuario/tu-repositorio/actions?query=workflow%3A%22Quarto+Publish%22)
[![GitHub Pages Status](https://img.shields.io/badge/Resultados-En%20Línea-blue)](https://tu-usuario.github.io/tu-repositorio/)
[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

**Autor:** Arturo Sánchez | **Retador:** Equipo Analisis de Gatos

---

## 🌟 Resumen del Proyecto: Ciencia Transparente y Automatizada

Este proyecto implementa un *pipeline* **CI/CD (Integración/Despliegue Continuo)** para el análisis de datos del experimento **ATLAS (CERN)**, utilizando **Python, marimo y Quarto**.

El objetivo es lograr la **máxima reproducibilidad y transparencia científica**. Cada `git push` desencadena una GitHub Action que:

1.  Descarga datos abiertos de ATLAS 13 TeV.
2.  Ejecuta el análisis (ej. redescubrimiento del Bosón Z).
3.  Genera gráficos y resultados usando el motor reactivo de **marimo**.
4.  Publica el informe y el sitio web completo en **GitHub Pages**. 

### 🔗 Resultados en Vivo

El informe y los gráficos interactivos generados por la última ejecución del CI están disponibles públicamente:

➡️ **[Ver el Sitio Web Publicado (Actualizado Automáticamente)](https://tu-usuario.github.io/tu-repositorio/)**

---

## ⚙️ Tecnologías y Características Clave

| Característica | Herramientas | Propósito en el Reto |
| :--- | :--- | :--- |
| **Análisis Numérico** | Python, `uproot`, `awkward-array`, `hist` | Lectura eficiente de datos ROOT y manipulación de estructuras de física de partículas. |
| **Interactividad** | **marimo** | Permite crear *widgets* reactivos y gráficos que se actualizan automáticamente en el informe. |
| **Publicación** | **Quarto** | Genera la documentación profesional y el sitio web estático (HTML, PDF, etc.). |
| **Reproducibilidad** | **Docker** | Asegura que el entorno de software (librerías y versiones) sea idéntico tanto en desarrollo local como en GitHub Actions. |
| **Automatización** | **GitHub Actions** | Orquesta el flujo completo de CI/CD: *Build* (Docker), *Analyze* (Python/marimo), *Render* (Quarto), *Deploy* (GitHub Pages). |


## 📁 Estructura del Repositorio

```

.
├── .github/workflows/
│   └── publish-site.yml       \# Workflow de CI/CD para Quarto y marimo.
├── analysis/                  \# Contiene archivos Python de marimo (.py) y Quarto (.qmd).
├── docs/                      \# Carpeta de salida (publicada por GitHub Pages).
├── index.qmd                  \# Página principal del sitio web con contenido marimo incrustado.
├── \_quarto.yml                \# Configuración general del proyecto Quarto.
├── requirements.txt           \# Lista de dependencias de Python.
└── Dockerfile                 \# Define el entorno de ejecución reproducible.
```

---

## 🐳 Instalación y Desarrollo Local (Usando Docker)

Para garantizar la **reproducibilidad**, todo el desarrollo se realiza dentro de un contenedor Docker preconfigurado.

### 1. Requisitos Previos

Asegúrate de tener **Docker** y **Docker Compose** instalados.

### 2. Configuración y Ejecución del Entorno

1.  **Construir la Imagen:**
    ```bash
    docker build -t fisico-remoto-env .
    ```

2.  **Ejecutar el Contenedor:** Inicia el contenedor y mapea el puerto y el volumen de trabajo para desarrollo local.

    ```bash
    docker run -it --rm -p 8080:8080 -v "$(pwd)":/app fisico-remoto-env /bin/bash
    ```

### 3. Vista Previa (Dentro del Contenedor)

Una vez dentro del contenedor, el entorno está listo. Ejecuta Quarto para compilar y visualizar el sitio:

```bash
# (Dentro del Contenedor)
quarto preview --port 8080 --host 0.0.0.0
````

Abre tu navegador en `http://localhost:8080`. Quarto vigilará los cambios en tus archivos.

### 4\. Flujo de Trabajo con marimo y Quarto

  * **Bloques Reactivos:** Inserta código Python con la clase `.marimo` en cualquier `.qmd` para añadir interactividad:

    \`\`\`python {.marimo}

    #### Celda marimo, si cambia 'x', todo lo que la usa se actualiza

    import marimo as mo
    x = mo.ui.slider(0, 10, 1, label="Valor de X")
    mo.md(f"El valor actual es: **{x.value}**")
    \`\`\`

  * **Exportación:** Convierte un *script* Python de marimo (`.py`) en un archivo Quarto (`.qmd`):

    ```bash
    # (Dentro del Contenedor)
    marimo export md analysis/mi_analisis.py -o analysis/mi_analisis.qmd
    ```

-----

## 🤖 Automatización y CI/CD

El workflow en `.github/workflows/publish-site.yml` maneja la automatización:

1.  **Activación:** `push` a la rama principal.
2.  **Job:** El *job* utiliza el entorno Docker o configura las dependencias necesarias, ejecuta `quarto render`, el cual procesa los análisis marimo.
3.  **Despliegue:** La acción de Quarto sube los archivos compilados a GitHub Pages.

Este sistema asegura que el sitio web y los resultados reflejen la versión más reciente del código del análisis.

-----

## 📚 Recursos y Licencia

  * **CERN Open Data:** Datasets de 13 TeV del experimento ATLAS [https://opendata.cern.ch/record/12360].
  * **Integración marimo:** [https://github.com/marimo-team/quarto-marimo](https://github.com/marimo-team/quarto-marimo)
  * **Guía de marimo:** [https://docs.marimo.io/](https://docs.marimo.io/)

Este repositorio está publicado bajo la licencia **MIT**. Consulta el archivo [`./LICENSE`] para detalles completos.
