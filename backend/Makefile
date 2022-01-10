.DEFAULT_GOAL := help

VERSION = $(shell make --no-print-directory version)

COLOR=\033[0;32m
NC=\033[0m

OBJECTS := $$(find . -type f \( -name *.py -not -path './.venv/*' \))

###### Development

.PHONY: dev
dev: ## Run development server
	docker-compose --file ./docker-compose.dev.yml up --detach
	uvicorn sit_igp_management_backend.main:app --reload --reload-dir ./sit_igp_management_backend

.PHONY: format
format: ## Format code
	@printf "\n${COLOR}=== Formatting code...${NC}\n"
	-poetry run pyupgrade --py38-plus $(OBJECTS)
	poetry run isort --settings-path pyproject.toml $(OBJECTS)
	poetry run black --config pyproject.toml $(OBJECTS)

.PHONY: test
test: test-lint test-unit test-safety ## Run all tests by decreasing priority

.PHONY: test-lint
test-lint: ## Run code linting tests
	@printf "\n${COLOR}=== Running code linting tests...${NC}\n"
	poetry run pyupgrade --py38-plus $(OBJECTS)
	poetry run isort --settings-path pyproject.toml $(OBJECTS)
	poetry run black --config pyproject.toml --diff --check $(OBJECTS)
	poetry run flake8 --config setup.cfg $(OBJECTS)
	poetry run pylint --rcfile pyproject.toml $(OBJECTS)
	poetry run mypy --config-file setup.cfg $(OBJECTS)

.PHONY: test-unit
test-unit: ## Run unit tests
	@printf "\n${COLOR}=== Running unit tests...${NC}\n"
	@poetry run pytest -c pyproject.toml

.PHONY: test-safety
test-safety: ## Run dependencies safety tests
	@printf "\n${COLOR}=== Running dependencies safety tests...${NC}\n"
	poetry check
	poetry run pip check
	poetry run safety check --full-report

###### Deployment


###### Clean up

.PHONY: clean
clean: ## Clean temporary files and directories
	@printf "\n${COLOR}=== Cleaning temporary files and directories...${NC}\n"
	@rm -rf dist
	@-find . -regex "^.*\(__pycache__\|\.pytest_cache\|\.?coverage\(\|\..*\)\)" -exec rm -rf {} +


###### Additional commands

.PHONY: version
version: ## Print the current version
	@cat pyproject.toml | grep -o '\([0-9]\+\.\?\)\{3\}' | head -1

ESCAPE = 
.PHONY: help
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/\n        $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-20s\033[0m %s\n", $$1, $$2}'
