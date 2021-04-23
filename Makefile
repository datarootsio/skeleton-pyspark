.PHONY: help create_environment requirements train predict
.DEFAULT_GOAL := help


###############################################################
# GLOBALS                                                     #
###############################################################


###############################################################
# COMMANDS                                                    #
###############################################################

clean: ## clean artifacts
	@echo ">>> cleaning files"


run-pipeline: clean

lint: ## flake8 linting and black code style
	@echo ">>> black files"
	@echo ">>> linting files"

coverage: ## create coverage report
	@echo ">>> running coverage pytest"
	coverage run --source=src -m pytest
	coverage report -m

test: ## run unit tests in the current virtual environment
	@echo ">>> running unit tests with the existing environment"
	tox

test-docker: ## run unit tests in docker environment
	@echo ">>> running unit tests in an isolated docker environment"

help: ## show help on available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
