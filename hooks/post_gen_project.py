#!/usr/bin/env python
"""Script running after creation of project"""

import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

#
if "{{ cookiecutter.setup_project }}" == "Yes - select this":
    subprocess.call('conda create -y -n "{{ cookiecutter.repo_name }}"')
    subprocess.call(
        'conda env update -n "{{ cookiecutter.repo_name }}" -f environment.yml'
    )
    subprocess.call("git init")
    subprocess.call("git lfs install")
    subprocess.call("pre-commit install")
