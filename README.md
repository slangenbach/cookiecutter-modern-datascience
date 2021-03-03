# Cookiecutter Modern Data Science
[Cookiecutter] template to create a data science project with modern, fast Python tools. This is a fork of the [modern data science template](https://github.com/crmne/cookiecutter-modern-datascience) orginally created by [Carmine Paolino](https://github.com/crmne) which is tailored to my workflow.

## Features
* [conda] to manage packages and environments in a platform agnostic way
* [Git LFS] to manage large files with git
* [Metaflow] to create elegant data pipelines and workflows
* [Weights and Biases] to track experiments
* Batteries included: [pandas], [numpy], [scipy], [scikit-learn], [seaborn], and [ipykernel] (required to work with [Jupyter Notebooks in VSCode](https://code.visualstudio.com/docs/python/jupyter-support)) already installed.
* Consistent code quality: [black], [isort], and [pylint] already installed.
* [Pytest] to write test.
* [GitHub Pages] to create a dedicated website for your project

## Prerequisites
* [miniconda] >= 4.9.2
* *Optional*: [VSCode](https://code.visualstudio.com/) >= 1.53.2

## Usage
Install the latest version of cookiecutter:
```bash
conda install -c conda-forge cookiecutter
```

Generate the project:
```bash
cookiecutter gh:sl/cookiecutter-modern-datascience
```

Activate the conda environment:
```bash
cd <repo_name>
conda activate dev  # activates dedicated conda env
```

*Optional*: Start [Weights and Biases] locally, if you don't want to use the cloud/on-premise version:
```bash
wandb local
```

Start working:
```bash
code .  # Replace code with your favourite editor
```

## Directory structure
```
├── data
│   ├── 0_external      <- Data from third party sources
│   ├── 1_raw           <- The original, immutable data dump
│   ├── 2_interim       <- Intermediate data that has been transformed in any way
│   └── 3_processed     <- Final, canoncial data for modeling
|
├── docs                <- Github pages website
|
├── flows               <- Data pipelines expressed as Metaflow flows
|
├── models              <- Serialized features, trained models, model predictions and summaries
|
├── notebooks           <- Jupyter notebooks
|
├── references          <- Documentation of raw/external data sources and all other explanatory materials
|
├── reports             <- Reports generated from analysis
│   ├── figures         <- Figures used in reports
|
├── .gitignore          <- GitHub's Python specific .gitignore with custom additions
├── LICENSE             <- License used for the project
├── README.md           <- Top-level README for developers involved in this project
└── environment.yml     <- conda environment file to reproduce the Python enviroment used for this project
```

## Limitations
* Post-generation hook is not yet working with conda
* Tests have not been adapted to changes conducted in this fork

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[conda]: https://docs.conda.io/en/latest/index.html
[Git LFS]: https://git-lfs.github.com/
[Metaflow]: https://metaflow.org/
[Weights and Biases]: https://www.wandb.com/
[pandas]: https://pandas.pydata.org/
[numpy]: https://numpy.org/
[scipy]: https://www.scipy.org/
[scikit-learn]: https://scikit-learn.org/stable/index.html
[seaborn]: https://seaborn.pydata.org/
[ipykernel]: https://ipython.readthedocs.io/en/stable/
[black]: https://github.com/psf/black
[isort]: https://github.com/timothycrosley/isort
[pylint]: https://www.pylint.org/
[Pytest]: https://docs.pytest.org/en/latest/
[GitHub Pages]: https://pages.github.com/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
