"""Localhost Monitor - macOS Menubar App for monitoring development servers."""

import tomllib
from pathlib import Path

def _get_version():
    """Read version from pyproject.toml"""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]

__version__ = _get_version()
