"""Test the creation of the project."""
import shutil
from pathlib import Path

import pytest
from cookiecutter import main

FILES = [
    ".gitignore",
    ".pre-commit-config.yaml",
    "LICENSE",
    "README.md",
    "environment.yml",
    "pyproject.toml",
]
FOLDERS = [
    Path("data"),
    Path("docs"),
    Path("flows"),
    Path("notebooks"),
    Path("references"),
    Path("reports"),
    Path("reports", "figures"),
]

CCDS_ROOT = Path(__file__).parent.parent.resolve()


@pytest.fixture(scope="function", name="project_dir")
def default_baked_project(tmp_path):
    """Fixture for creation and teardown of the project."""
    out_dir = tmp_path / "data-project"
    out_dir.mkdir()

    main.cookiecutter(
        CCDS_ROOT.as_posix(),
        no_input=True,
        extra_context={"setup_project": "No - for testing purposes only"},
        output_dir=out_dir,
    )

    # default project name is project_name
    yield out_dir / "project_name"

    # cleanup after
    shutil.rmtree(out_dir)


def test_files(project_dir):
    """Are the files there?"""
    for file_path in FILES:
        final_path = project_dir / file_path

        assert final_path.is_file()
        assert no_curlies(final_path)


def test_folders(project_dir):
    """Are the folders there?"""
    for folder in FOLDERS:
        final_path = project_dir / folder

        assert final_path.is_dir()
        assert no_curlies(final_path)


def no_curlies(filepath: Path):
    """Utility to make sure no curly braces appear in a file.
    That is, was jinja able to render everthing?"""
    template_strings = ["{{", "}}", "{%", "%}"]

    if any([s in filepath.name for s in template_strings]):
        return False

    if filepath.is_file():
        template_strings_in_file = [s in filepath.read_text() for s in template_strings]
        return not any(template_strings_in_file)

    return True
