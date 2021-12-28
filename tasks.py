"""Tasks file for `invoke`.

Notes:  Type-Hinting is not able to be used until
https://github.com/pyinvoke/invoke/issues/357 is closed.
"""

import os

from invoke import task


@task
def docs(context):
    if os.name == "nt":  # if windows...
        context.run(".\\docs\\make.bat html")
    else:
        context.run("cd docs && make html && cd ..")


@task
def test(context):
    context.run("pytest --cov=pytemplate tests/")


@task
def install_precommit(context):
    context.run("pre-commit install")


@task
def tox(context):
    context.run("tox")


@task(pre=[install_precommit])
def init(context):
    print("Installing pre-commit...")
