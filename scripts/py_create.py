#!/usr/bin/env python3
import os
import sys


def create_problem(number):
    # Pad problem number with zeros
    padded_number = str(number).zfill(4)

    # Create directory
    dir_path = f"py/{padded_number}"
    os.makedirs(dir_path, exist_ok=True)

    # Create BUILD.bazel
    build_content = """load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_test(
    name = "test",
    size = "small",
    srcs = ["test.py"],
    imports = ["./"],
    main = "test.py",
    deps = [":main"],
)

py_library(
    name = "main",
    srcs = ["main.py"]
)
"""

    # Create main.py
    main_content = """from typing import List

class Solution:
    def solution(self) -> int:
        return 0
"""

    # Create test.py
    test_content = """import unittest
from main import Solution

class Test{number}(unittest.TestCase):
    def test(self):
        testcases = [
            [0, 0]  # [input, expected]
        ]

        for i in testcases:
            input_val, expected = i
            s = Solution()
            actual = s.solution(input_val)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
""".format(number=padded_number)

    # Write files
    with open(os.path.join(dir_path, "BUILD.bazel"), "w") as f:
        f.write(build_content)

    with open(os.path.join(dir_path, "main.py"), "w") as f:
        f.write(main_content)

    with open(os.path.join(dir_path, "test.py"), "w") as f:
        f.write(test_content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 create_py_problem.py <problem_number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        create_problem(number)
        print(f"Created Python problem {number} successfully!")
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)


if __name__ == "__main__":
    main()
