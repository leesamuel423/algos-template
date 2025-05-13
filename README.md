# leesamuel423 algos template

A multi-language algorithm practice template using Bazel to manage builds and tests across Python, Go, Java, and C++.

## Languages Supported

- Python
- Go
- Java
- C++

## Features

- Consistent structure across all supported languages
- Automated project setup for new problems
- Bazel build system for reliable builds and testing
- Example solutions ([0001]) to demonstrate the template pattern

## Setup

Before using the template, set execute permissions for the scripts:

```bash
make setup
```

## Usage

### Creating New Problems

Create a new problem solution template using the following commands:

```bash
make go 123    # Create a new Go problem #123
make java 123  # Create a new Java problem #123
make py 123    # Create a new Python problem #123
make cpp 123   # Create a new C++ problem #123
```

Each command will:
- Create a directory with the appropriate problem number (e.g., `go/0123/`)
- Generate template solution and test files
- Set up Bazel build configuration

### Running Tests

To run all tests in the project:

```bash
make test
```

To run tests for a specific problem:

```bash
make test go/0001  # Test Go problem #0001
make test java/0123  # Test Java problem #123
```

### Cleanup

Remove Bazel build artifacts:

```bash
make clean
```

### Getting Help

To display all available commands:

```bash
make help
```

## Project Structure

```
.
├── cpp/          # C++ solutions
├── go/           # Go solutions
├── java/         # Java solutions
├── py/           # Python solutions
└── scripts/      # Problem generation scripts
```

Each problem directory follows a consistent structure:

```
language/####/
├── BUILD.bazel   # Bazel build configuration
├── solution.*    # Solution implementation file
└── test.*        # Test file
```

## Real Use Case

See [leesamuel423/algo-grind](https://github.com/leesamuel423/algo-grind) as an example
