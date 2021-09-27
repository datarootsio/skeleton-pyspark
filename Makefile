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


RUN_ARGS     ?= dev
POETRY_PREFIX?= poetry run
submit: ## Submits the job assuming the cluster has all the dependencies
	@echo ">>> Submits the job without dependencies"
	$(POETRY_PREFIX) spark-submit run.py $(RUN_ARGS)

build: ## create the wheel
	@echo ">>> packaging library"
	poetry build -vv

submit_with_dep: clean_docker pack_req submit_py_zip clean_docker

clean_docker: ## Cleans the docker images if they were created for the dependency
	@echo ">>> Cleans the docker images and instances"
	docker rm build_dep || true
	docker rmi -f skeleton-pyspark_build_dep || true

pack_req: ## Packs the dependencies into a zip file
	@echo ">>> Packs the dependencies in a zip file"
	docker-compose up build_dep

submit_py_zip: ## Submits the job with --py-files archived at package.zip
	@echo ">>> Submits the packaged zip file to add any additional modules"
	$(POETRY_PREFIX) spark-submit --py-files package.zip run.py $(RUN_ARGS)

help: ## show help on available commands
	@grep -E '^[a-zA-Z.%_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

