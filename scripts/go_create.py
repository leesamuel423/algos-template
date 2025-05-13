#!/usr/bin/env python3
import os
import sys


def create_problem(number):
    # Pad problem number with zeros
    padded_number = str(number).zfill(4)

    # Create directory
    dir_path = f"go/{padded_number}"
    os.makedirs(dir_path, exist_ok=True)

    # Create BUILD.bazel
    build_content = """load("@io_bazel_rules_go//go:def.bzl", "go_library", "go_test")

go_library(
    name = "solution",
    srcs = ["solution.go"],
    visibility = ["//visibility:public"],
)

go_test(
    name = "test",
    size = "small",
    srcs = ["solution_test.go"],
    embed = [":solution"],
)
""".format(number=padded_number)

    # Create solution.go
    solution_content = """package solution

func Solution(input int) int {
    return 0
}
"""

    # Create solution_test.go
    test_content = """package solution

import "testing"

func TestSolution(t *testing.T) {
    testCases := []struct {
        name     string
        input    int
        expected int
    }{
        {
            name:     "Example 1",
            input:    0,
            expected: 0,
        },
        {
            name:     "Example 2",
            input:    1,
            expected: 0,
        },
    }

    for _, tc := range testCases {
        t.Run(tc.name, func(t *testing.T) {
            if got := Solution(tc.input); got != tc.expected {
                t.Errorf("Solution() = %v, want %v", got, tc.expected)
            }
        })
    }
}
"""

    # Write files
    with open(os.path.join(dir_path, "BUILD.bazel"), "w") as f:
        f.write(build_content)

    with open(os.path.join(dir_path, "solution.go"), "w") as f:
        f.write(solution_content)

    with open(os.path.join(dir_path, "solution_test.go"), "w") as f:
        f.write(test_content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 create_go_problem.py <problem_number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        create_problem(number)
        print(f"Created Go problem {number} successfully!")
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)


if __name__ == "__main__":
    main()
