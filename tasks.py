"""Tasks file for `invoke`.

Notes:  Type-Hinting is not able to be used until
https://github.com/pyinvoke/invoke/issues/357 is closed.
"""

import os

from invoke import Context, task


@task
def docs(context: Context) -> None:
    """Generate Sphinx documentation."""
    if os.name == "nt":  # if windows...
        context.run(".\\docs\\make.bat html")
    else:
        context.run("cd docs && make html && cd ..")


@task
def test(context: Context) -> None:
    """Run Pytest."""
    context.run("pytest --cov=stuff tests/")


@task
def install_precommit(context: Context) -> None:
    """Install pre-commit into githooks."""
    context.run("pre-commit install")


@task
def tox(context: Context) -> None:
    """Run Tox."""
    context.run("tox")


@task(pre=[install_precommit])
def init(_context: Context) -> None:
    """Init the repository.

    - Install pre-commit hooks.
    """
    print("Installing pre-commit...")
