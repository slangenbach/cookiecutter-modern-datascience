#!/usr/bin/env python

import os
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

if "{{ cookiecutter.license }}" == "Not open source":
    (PROJECT_DIRECTORY / "LICENSE").unlink()

if "{{ cookiecutter.setup_project }}" == "Yes - select this":
    os.system("git init")
    os.system('conda create --name "{{ cookiecutter.repo_name }}" --f environment.yml')
