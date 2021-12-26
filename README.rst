===========
PyTemplate
===========

What is this?
=============

**The Problem**: Whenever I needed an up-to-date template to start a new Python project (module, package, etc.) in, I'd start it from scratch each time.  *This package is meant to be an (updated) template to use for Python modules/packages.*

What does this include?
=======================
- Linting and Formatting.
    - Pylint_ is a code analysis tool
    - Black_ is an uncompromising formatter
    - flake8_ is a style guide enforcement tool which encludes McCabe (complexity checker)
    - mypy_ is a static type checker (enforces type hints)

- Testing Integration
    - **Pytest**.

Why is XYZ file here?
=====================
- ``.flake8``: Because of `this frustrating thread <https://github.com/PyCQA/flake8/issues/234>`_.
- ``.pre-commit-config``: Required my ``pre-commit``, read more `here <https://pre-commit.com/#intro>`_.

What Still Needs Work?
======================


.. _PyLint: https://pylint.org/
.. _Black: https://github.com/psf/black/
.. _flake8: https://flake8.pycqa.org/en/latest/
