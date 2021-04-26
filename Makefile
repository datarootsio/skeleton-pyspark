.PHONY: help docs
.DEFAULT_GOAL := help

clean: ## clean artifacts
	@echo ">>> cleaning files"

run-pipeline: clean lint coverage

lint: ## flake8 linting and black code style
	@echo ">>> black files"
	poetry run black src tests
	@echo ">>> linting files"
	poetry run flake8 src tests

coverage: ## create coverage report
	@echo ">>> running coverage pytest"
	poetry run coverage run --source=src -m pytest
	poetry run coverage xml

bandit: ## discover common security issues
	@echo ">>> discover common security issues"
	poetry run bandit src

test: ## run unit tests in the current virtual environment
	@echo ">>> running unit tests with the existing environment"
	poetry run pytest

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


help: ## show help on available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
