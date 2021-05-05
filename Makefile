.PHONY: help docs submit
.DEFAULT_GOAL := help

run-pipeline: lint mypy bandit coverage sphinx.html

lint: ## flake8 linting and black code style
	@echo ">>> black files"
	poetry run black src tests run.py
	@echo ">>> linting files"
	poetry run flake8 --extend-ignore=ANN101 src tests run.py

mypy: ## static type-check with mypy
	@echo ">>> statically analyses code with mypy"
	poetry run mypy -m run

bandit: ## discover common security issues
	@echo ">>> discover common security issues"
	poetry run bandit src run.py

test: ## run tests in the current virtual environment
	@echo ">>> running tests with the existing environment"
	poetry run pytest

coverage: ## create coverage report
	@echo ">>> running coverage pytest"
	poetry run coverage run --source=src -m pytest
	poetry run coverage xml


###########################################################################
#### SPHINX Documentation

SPHINXOPTS    ?=
SPHINXBUILD   ?= poetry run sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = docs/build

sphinx.%: ## sphinx documentation wildcard (eg. sphinx.html)
	@echo ">>> Sphinx documentation. $*"
	@$(SPHINXBUILD) -M $* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#############################################################################


RUN_ARGS     ?= --env dev
submit: ## Packs the requirements in a wheel and submits the job
	@echo ">>> TODO: pack requirements in a whl/zip file and submit to the cluster with --py-files"
	spark-submit run.py $(RUN_ARGS)

help: ## show help on available commands
	@grep -E '^[a-zA-Z.%_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

