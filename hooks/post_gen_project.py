#!/usr/bin/env python
"""Script running after creation of project"""

import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

#
if "{{ cookiecutter.setup_project }}" == "Yes - select this":
    print("Setting up conda environment")
    subprocess.run(
        [
            "conda",
            "create",
            "-n",
            "{{ cookiecutter.repo_name }}",
            "-f",
            "environment.yml",
        ]
    )
    print("Initializing Git repository")
    subprocess.run(["git", "init"])
    print("Installig Git LFS")
    subprocess.run(["git", "lfs", "install"])
    print("Installing pre-commit hooks")
    subprocess.run(["pre-commit", "install"])
