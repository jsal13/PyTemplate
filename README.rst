===========
PyTemplate
===========

What is this?
=============

**The Problem**: Whenever I needed an up-to-date template to start a new Python project (module, package, etc.) in, I'd start it from scratch each time.  *This package is meant to be an (updated) template to use for Python modules/packages.*

How Do I Use This?
==================

First...
--------
    - Rename "pytemplate" with the name of your package.
    - Find-Replace all uses of "pytemplate" with the name of your package in this project.

Then...
-------
In your terminal,

1. Install Poetry.  ``pip install poetry``.
2. In the root, create the poetry venv.  ``poetry install``.
3. Use the Poetry Shell to open the project in VSCode.  ``poetry shell``, then ``code .``.
    - It will probably work in other IDEs, but I haven't tried it yet.
4. (*Optional*) To install the pre-commit checks for git, run ``pre-commit install``.
5. (*Optional*) To run Sphinx, run the makefile in ``docs``.  For example, ``cd docs && make html``.
    - On Windows, you can use ``.\docs\make.bat html``.
6. (*Optional*) To run ``tox``, use the command ``tox``.  To configure this, check out its section in ``pyproject.toml``
7. (*Optional*) If you want to Dockerize anything, I've included a ``Dockerfile`` for using Poetry and Python, a ``docker-entrypoint.sh`` for exec, and a basic ``docker-compose`` file for composition

**Notes**:
    - To Remove the Vertical Line that's at Column 88 for VSCode, remove the "Editor Rules" line in ``.vscode/settings.json``.
    - To run tests, you can use the VSCode test tab on the left-hand side (looks like a beaker).
        - To run coverage, you can use the terminal command ``pytest --cov=pyproject tests/``
    - Precommit may format your code and say the commit failed; run the commit again and it will (most likely) pass.


What does this include?
=======================
- Venv and Build Tools
    - Poetry_ allows us to easily manage a venv and build our things quickly.

- Linting and Formatting
    - Pylint_ is a code analysis tool
    - Black_ is an uncompromising formatter
    - flake8_ is a style guide enforcement tool which encludes McCabe (complexity checker)
    - mypy_ is a static type checker (enforces type hints)

- Testing Integration
    - Pytest_ for testing and Pytest-Cov_ for coverage
    - Tox_ for venv management and testing

- Documentation
    - Sphinx_ with Sphinx-AutoAPI_ to generate things automatically

- Containerization
    - Docker_ and docker-compose to create containers if needed.

What's this XYZ Config file?
=====================
- ``.flake8``: Because of `this frustrating thread <https://github.com/PyCQA/flake8/issues/234>`_.
- ``.pre-commit-config``: Required my ``pre-commit``, read more `here <https://pre-commit.com/#intro>`_.
- ``pyproject.toml``: The new standard for Python configuation.  **There's a lot you can edit in here, so check it out.**
- ``poetry.lock``: A poetry file which contains specifics about what's installed.  Poetry generates this when you install it.
- ``.vscode/``: A folder for custom vscode configurations.
- ``Dockerfile``, ``docker-entrypoint.sh``, ``docker-compose.yaml``: These are all Docker-related files, all optional unless you'd like to use Docker.


What Still Needs Work?
======================
- Better Pytest examples.
- There is a weird bug in VSCode that sometimes makes Pylance extremely slow on my PC.  Check this out.
- Github Actions.

.. _Black: https://github.com/psf/black/
.. _Docker: https://www.docker.com/
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _mypy: http://mypy-lang.org/
.. _Poetry: https://python-poetry.org/docs/basic-usage/
.. _PyLint: https://pylint.org/
.. _Pytest-Cov: https://pytest-cov.readthedocs.io/en/latest/
.. _Pytest: https://docs.pytest.org/en/6.2.x/
.. _Sphinx-AutoAPI: https://github.com/readthedocs/sphinx-autoapi
.. _Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _Tox: https://tox.wiki/en/latest/
