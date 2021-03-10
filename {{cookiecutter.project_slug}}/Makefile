.PHONY: clean clean-test clean-pyc docs help list
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help: ## print a list of relevant targets
	@echo "clean		remove all build artifacts"
	@echo "clean-pyc	clean project of all pyc files"
	@echo "clean-test	clean pytest cache"
	@echo "lint		run python linter"
	@echo "test		run python tests"
	@echo "docs		generate sphinx documentation"

clean: clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 cookiecutter_houdini_project tests

test: ## run tests quickly with the default Python
	python setup.py test

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/pdg_export.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ python/
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html
