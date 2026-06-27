# About CryoEM Playbook

CryoEM Playbook is a collection of interactive computational practicals for the **High Resolution Imaging** course at TU Delft.

## Technology

Notebooks are embedded via [JupyterLite](https://jupyterlite.readthedocs.io/) using the [mkdocs-jupyterlite](https://nickcrews.github.io/mkdocs-jupyterlite/) plugin. All code runs in the browser using [Pyodide](https://pyodide.org/) — a WebAssembly port of CPython. No server or local installation is required.

## Dependencies

All practicals use standard scientific Python packages that ship with Pyodide:

- `numpy`, `matplotlib`, `scipy` — numerics and plotting
- `ipywidgets` — interactive sliders and dropdowns

## Source

Source notebooks and course materials are maintained by Arjen Jakobi (TU Delft).
