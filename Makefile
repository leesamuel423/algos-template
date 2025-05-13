# Default shell
SHELL := /bin/bash

# Colors for pretty printing
GREEN := \033[0;32m
NC := \033[0m # No Color

.PHONY: help go java py cpp test clean

help:
	@echo "Usage:"
	@echo "  make go 123    	- Create new Go problem"
	@echo "  make java 123  	- Create new Java problem"
	@echo "  make py 123    	- Create new Python problem"
	@echo "  make cpp 123   	- Create new C++ problem"
	@echo "  make test      	- Run all tests"
	@echo "  make test go/0001 	- Run specific test"
	@echo "  make clean     	- Clean Bazel artifacts"

# Create new problems
go:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make go 123"; \
		exit 1; \
	fi
	@echo "Creating Go problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/go_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created Go problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

java:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make java 123"; \
		exit 1; \
	fi
	@echo "Creating Java problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/java_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created Java problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

py:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make py 123"; \
		exit 1; \
	fi
	@echo "Creating Python problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/py_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created Python problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

cpp:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Please provide a problem number: make cpp 123"; \
		exit 1; \
	fi
	@echo "Creating C++ problem $(filter-out $@,$(MAKECMDGOALS))..."
	@./scripts/cpp_create.py $(filter-out $@,$(MAKECMDGOALS))
	@echo -e "${GREEN}Successfully created C++ problem $(filter-out $@,$(MAKECMDGOALS))${NC}"

# Testing
test:
	@if [ -z "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		echo "Running all tests..."; \
		bazel test //...; \
	else \
		echo "Running test for $(filter-out $@,$(MAKECMDGOALS))..."; \
		bazel test //$(filter-out $@,$(MAKECMDGOALS)):test; \
	fi

# Cleanup
clean:
	@echo "Cleaning Bazel artifacts..."
	@bazel clean

# This allows for arbitrary arguments
%:
	@:
