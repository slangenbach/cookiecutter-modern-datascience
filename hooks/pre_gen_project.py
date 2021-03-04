#!/usr/bin/env python
"""Script running before creation of project"""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

MODULE_NAME = "{{ cookiecutter.repo_name }}"

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(
        f"ERROR: The project slug {MODULE_NAME} is not a valid Python module name. "
        "Please do not use a - (hyphen) and use _ (underscore) instead."
    )

    # Exit to cancel project
    sys.exit(1)
