# Cookiecutter Modern Data Science
[Cookiecutter] template to create a data science project with modern, fast Python tools.  
This is a fork of the [modern data science template](https://github.com/crmne/cookiecutter-modern-datascience)
originally created by [Carmine Paolino](https://github.com/crmne) which is tailored to my workflow.

## Features
* [Conda] and [renv] to manage Python, R and other packages/environments in a platform agnostic way
* [Git LFS] to manage large files with git
* [Metaflow] to create elegant data pipelines and workflows
* [MLflow] to track experiments and log artifacts
* Batteries included: [pandas], [numpy], [scipy], [scikit-learn], [seaborn], and [ipykernel]
(required to work with [Jupyter Notebooks in VSCode](https://code.visualstudio.com/docs/python/jupyter-support)) already installed.
* Consistent code quality: [black], [isort], and [pylint] already installed and enforced using [pre-commit] hook (even for Jupyter Notebooks thanks to [nbQA])
* [Pytest] to write test.
* [GitHub Pages] to create a dedicated website for your project

## Prerequisites
* [Cookiecutter] >= 1.7.2
* [miniconda] >= 4.9.2 (for setting up Python environments)
* [R] >= 4.0.4 (for setting up R environments)

## Usage
Install the latest version of cookiecutter:

    conda install -c conda-forge cookiecutter

Generate the project:

    cookiecutter gh:sl/cookiecutter-modern-datascience

Activate the conda environment:

    cd <repo_name>
    conda activate <repo_name>

*Optional*: Start [MLflow] locally

    mlflow server

*Optional*: Track your data, e.g. CSV files, with Git LFS

    git lfs track "*.csv"

Start working:

    code .  # Replace code with your favourite editor

## Directory structure
The directory structure contains only essential files and folders.
Instead of using lots of nested subfolders, tools like [Metaflow] and [MLflow] take care of these tasks for us.

```
├── artifacts           <- Serialized features and models
│   
├── data                <- Data used in this project
│   ├── external        <- All data from external sources
│   ├── raw             <- Original, immutable data dumps from raw/external data sources
│   ├── interim         <- Cleaned data saved in *parquet* format
│   ├── processed       <- Preprocessed data used for model building
│ 
├── docs                <- Github pages website
│
├── flows               <- Data pipelines expressed as Metaflow flows
│ 
├── notebooks           <- Jupyter/R notebooks
│ 
├── references          <- Documentation of data sources and all other explanatory materials
│ 
├── reports             <- Reports generated from analysis done in notebooks
│   ├── figures         <- Figures used in reports
│ 
├── .gitignore          <- GitHub's Python/R specific .gitignore customized for tools used in this project
├── LICENSE             <- License used for the project
├── README.md           <- Top-level README for developers working with this project
├── environment.yml     <- conda environment file to reproduce the Python enviroment used for this project
└── renv.lock           <- renv file to reproduce the R enviroment used for this project
```

## References
* [Github project](https://github.com/slangenbach/cookiecutter-modern-datascience/projects/1)

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Conda]: https://docs.conda.io/en/latest/index.html
[Git LFS]: https://git-lfs.github.com/
[Metaflow]: https://metaflow.org/
[MLflow]: https://mlflow.org/
[pandas]: https://pandas.pydata.org/
[numpy]: https://numpy.org/
[scipy]: https://www.scipy.org/
[scikit-learn]: https://scikit-learn.org/stable/index.html
[seaborn]: https://seaborn.pydata.org/
[ipykernel]: https://ipython.readthedocs.io/en/stable/
[black]: https://github.com/psf/black
[isort]: https://github.com/timothycrosley/isort
[pylint]: https://www.pylint.org/
[pre-commit]: https://pre-commit.com/
[nbQA]: https://github.com/nbQA-dev/nbQA
[Pytest]: https://docs.pytest.org/en/latest/
[GitHub Pages]: https://pages.github.com/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[R]: https://www.r-project.org/
[renv]: https://rstudio.github.io/renv/index.html
