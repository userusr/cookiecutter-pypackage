.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

APP_DIR={{ cookiecutter.project_slug }}
TESTS_DIR=tests/

VENV_DIR ?= venv
ifeq ($(wildcard ${VENV_DIR}),)
	VENV_BIN=
else
	VENV_BIN=./${VENV_DIR}/bin/
endif

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	${VENV_BIN}/flake8 {{ cookiecutter.project_slug }} tests

venv: ## make python virtualenv
	python -m venv ${VENV_DIR}
	${VENV_BIN}pip install -U pip pip-tools

pip-requirements: ## compile requirements with pip-compile
	${VENV_BIN}pip-compile
	${VENV_BIN}pip-compile requirements_dev.in
	${VENV_BIN}pip-sync requirements*.txt

test: ## run tests quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	${VENV_BIN}pytest
{%- else %}
	${VENV_BIN}python setup.py test
{%- endif %}

test-all: ## run tests on every Python version with tox
	${VENV_BIN}tox

coverage: ## check code coverage quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	${VENV_BIN}coverage run --source {{ cookiecutter.project_slug }} -m pytest
{%- else %}
	${VENV_BIN}coverage run --source {{ cookiecutter.project_slug }} setup.py test
{%- endif %}
	${VENV_BIN}coverage report -m
	${VENV_BIN}coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	${VENV_BIN}sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	${VENV_BIN}watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	${VENV_BIN}twine upload dist/*

dist: clean ## builds source and wheel package
	${VENV_BIN}python setup.py sdist
	${VENV_BIN}python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	${VENV_BIN}python setup.py install
