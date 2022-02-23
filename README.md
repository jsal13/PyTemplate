# PyTemplate

## What is this?

**The Problem**: Whenever I needed an up-to-date template to start a new Python project (module, package, etc.) in, I'd start it from scratch each time.  This package is the cookie-cutter template I use for getting started quickly.

## Opinionated Code Process.
There is a strong emphasis on linting and testing in this package, as well as CI/CD.  Roughly,

```graph TD
   A["New Script"]
   B["Write Code"]
   C["Auto Lint & Format"]
   D["Precommit Tests"]
   E["Github Actions for CI/CD"]
   A --> B
   B --> |On Save| C --> B
   B --> |On Commit| D 
   D --> |On Push| E
   ```


## How Do I Use This?

### First...
- Rename "pytemplate" with the name of your package
- Find-Replace all uses of "pytemplate" with the name of your package in this project

### Then...
In terminal,

1. Install [Poetry][8]:

```
pip install poetry
```

2. In the root, create the poetry venv:

```
poetry install
```

3. Initialize the repo:

```
invoke init
```

4. Use the Poetry Shell to open the project in VSCode:

```
poetry shell
code .
```

(OPTIONAL) Some Other Things You Can Do
----------------------------------------

For many optional things, we use [Invoke][5] to call basic commands.  See the docs and the ``tasks.py`` file in the root directory for more information on Invoke.  It's also easy to make your own basic commands!

- To Remove / Modify the [Github Actions][4] file, delete / edit the ``.github\workflows\sample-github-action.yml`` file.

- To run tests, you can use the VSCode test tab on the left-hand side (looks like a beaker)
    - To run testing + coverage, on the terminal:

```
invoke test
```

- To run [Sphinx][14], use the command:

```
invoke docs
```

- To configure [Tox][15], check out its section in ``pyproject.toml`` and run:

```
tox
# or `invoke tox`
```

- If you want to [Dockerize][2] anything, I've included a ``Dockerfile`` for using Poetry and Python, a ``docker-entrypoint.sh`` for exec, and a basic ``docker-compose`` file for composition


## What does this cookie-cutter include?
### Venv and Build Tools
- [Poetry][8] allows us to easily manage a venv and build our things quickly.

### Linting and Formatting
- [Pylint][10] is a code analysis tool
- [Black][1] is an uncompromising formatter
- [flake8][3] is a style guide enforcement tool which encludes McCabe (complexity checker)
- [mypy][7] is a static type checker (enforces type hints)
- [pydocstyle][9] is a docstring linter
- [isort][6] sorts imports

### Testing Integration
- [Pytest][12] for testing and [Pytest-Cov][11] for coverage
- [Tox][15] for venv management and testing

### Documentation
- [Sphinx][14] with [Sphinx Auto-API][13] to generate things automatically

### CLI
- [Invoke][5] allows for easy CLI construction

### Containerization
- [Docker][2] with docker-compose to create containers if needed

## What do the config files do...?
- ``pyproject.toml``: The new standard for Python configuation
    - **There's a lot you can edit, so check it out**
- ``.flake8``: Required because of [this frustrating thread](https://github.com/PyCQA/flake8/issues/234)
- ``.pre-commit-config``: Required by ``pre-commit``, read more [here](https://pre-commit.com/#intro)
- ``poetry.lock``: A poetry file which contains specifics about what's installed.  Poetry generates this when you install it
- ``.vscode/``: A folder for custom vscode configurations
- ``Dockerfile``, ``docker-entrypoint.sh``, ``docker-compose.yaml``: These are all Docker-related files, all optional unless you'd like to use Docker
- ``.github/workflows/sample-github-action.yml`` is a sample for [Github Actions][4] which currently runs [tox][15] (and therefore [Pytest][10]), but can be configured to run whatever you'd like
- ``tasks.py`` is used by [Invoke][5] to create CLI commands, check out the link below to create your own


### What Still Needs Work in this Template?
- [ ] Better Pytest examples.

[1]: <https://github.com/psf/black/> "Black"
[2]: <https://www.docker.com/> "Docker"
[3]: <https://flake8.pycqa.org/en/latest/> "Flake8"
[4]: <https://github.com/features/actions/> "Github Actions"
[5]: <https://docs.pyinvoke.org/en/stable/index.html> "Invoke"
[6]: <https://pycqa.github.io/isort/> "isort"
[7]: <http://mypy-lang.org/> "Mypy"
[8]: <https://python-poetry.org/docs/basic-usage/> "Poetry"
[9]: <http://www.pydocstyle.org/en/stable/> "Pydocstyle"
[10]: <https://pylint.org/> "Pylint"
[11]: <https://pytest-cov.readthedocs.io/en/latest/> "Pytest-Cov"
[12]: <https://docs.pytest.org/en/6.2.x/> "Pytest"
[13]: <https://github.com/readthedocs/sphinx-autoapi> "Sphinx Auto-API"
[14]: <https://www.sphinx-doc.org/en/master/usage/quickstart.html> "Sphinx"
[15]: <https://tox.wiki/en/latest/> "Tox"
