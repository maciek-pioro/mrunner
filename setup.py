import re
from pathlib import Path

from setuptools import find_packages, setup


def read_version() -> str:
    """Extract package version from mrunner/__init__.py."""
    version_file = Path(__file__).parent / "mrunner" / "__init__.py"
    content = version_file.read_text(encoding="utf8")
    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if not match:
        raise RuntimeError("Unable to find __version__ in mrunner/__init__.py")
    return match.group(1)

setup(
    name="mrunner",
    version=read_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "cryptography>=2.2.2",
        "PyYAML",
        "fabric",
        "path<17.0",
        "jinja2",
        "six",
        "attrs>=17.3",
        "click",
        "docker",
        "kubernetes>=5.0.0",
        "google-cloud",
        "termcolor",
        "pyperclip",
        "cloudpickle",
        "neptune>=1.0.0",
        "munch",
        "gin-config",
        "gitignore_parser",
    ],
    entry_points={
        "console_scripts": ["mrunner=mrunner.cli.mrunner_cli:cli"],
    },
    extras_require={
        "dev": ["black", "isort", "pre-commit"],
        "doc": ["sphinx-rtd-theme", "sphinx", "myst_parser"],
    },
)
