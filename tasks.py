"""Tasks file for `invoke`.

Notes:  Type-Hinting is not able to be used until
https://github.com/pyinvoke/invoke/issues/357 is closed.
"""

import os

from invoke import task


@task
def docs(context) -> None:  # type: ignore
    """Generate Sphinx documentation."""
    if os.name == "nt":  # if windows...
        context.run(".\\docs\\make.bat html")
    else:
        context.run("cd docs && make html && cd ..")


@task
def test(context) -> None:  # type: ignore
    """Run Pytest."""
    context.run("pytest --cov=stuff tests/")


@task
def install_precommit(context) -> None:  # type: ignore
    """Install pre-commit into githooks."""
    context.run("pre-commit install")


@task
def tox(context) -> None:  # type: ignore
    """Run Tox."""
    context.run("tox")


@task(pre=[install_precommit])
def init(_context) -> None:  # type: ignore
    """Init the repository.

    - Install pre-commit hooks.
    """
    print("Installing pre-commit...")
