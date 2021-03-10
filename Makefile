.PHONY: help bake replay noinput docs
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help: ## print a list of targets
	@echo "bake	generate project using defaults"
	@echo "replay	replay last cookiecutter run"
	@echo "noinput	generate project files without prompting for input"
	@echo "docs	generate sphinx documentation"

bake:
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

replay: BAKE_OPTIONS=--replay
replay: bake
	;

noinput: BAKE_OPTIONS=--no-input
noinput: bake
	;

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/cookiecutter-houdini-project.rst
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html
