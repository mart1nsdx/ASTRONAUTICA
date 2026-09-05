# ASTRONAUTICA

Código de apoyo del capítulo **«Métodos computacionales en Ingeniería Aeroespacial»**.

Este repositorio contiene los scripts que generan las figuras y las simulaciones
que acompañan al texto. La estructura de carpetas sigue una a una las secciones
del capítulo.

## Secciones

| Carpeta | Sección |
|---|---|
| [`01_integracion_numerica_ecuaciones_movimiento/`](01_integracion_numerica_ecuaciones_movimiento/) | §1 — Integración numérica de ecuaciones de movimiento |
| [`02_estimacion_de_estados/`](02_estimacion_de_estados/) | §2 — Estimación de estados |
| [`03_aerodinamica_computacional/`](03_aerodinamica_computacional/) | §3 — Aerodinámica computacional |
| [`04_aeroelasticidad_computacional/`](04_aeroelasticidad_computacional/) | §4 — Aeroelasticidad computacional |
| [`05_arquitectura_de_un_simulador/`](05_arquitectura_de_un_simulador/) | §5 — Arquitectura de un simulador |

Cada carpeta contiene los scripts de su sección y una subcarpeta `figuras/`
con las imágenes que estos generan.

## Requisitos

```bash
python3 -m venv venv
./venv/bin/pip install numpy matplotlib
```

## Uso

Cada script se ejecuta por sí solo y guarda su figura en `figuras/`:

```bash
cd 01_integracion_numerica_ecuaciones_movimiento
python3 metodo_euler.py
```
