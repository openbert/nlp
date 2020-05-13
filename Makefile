.PHONY: dependencies
dependencies:
	pip install -r requirements.txt

.PHONY: dev-dependencies
dev-dependencies:
	pip install -r requirements-dev.txt

.PHONY: test
test: dependencies dev-dependencies
	pytest
