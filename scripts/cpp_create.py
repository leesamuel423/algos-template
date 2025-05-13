#!/usr/bin/env python3
import os
import sys


def create_problem(number):
    # Pad problem number with zeros
    padded_number = str(number).zfill(4)

    # Create directory
    dir_path = f"cpp/{padded_number}"
    os.makedirs(dir_path, exist_ok=True)

    # Create BUILD.bazel
    build_content = """cc_library(
    name = "solution",
    hdrs = ["solution.h"],
    visibility = ["//visibility:public"],
)

cc_test(
    name = "test",
    size = "small",
    srcs = ["test.cc"],
    deps = [
        ":solution",
        "@com_google_googletest//:gtest_main",
    ],
)
"""

    # Create solution.h
    solution_content = """#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>

class Solution {
public:
    int solution(int input) {
        return 0;
    }
};

#endif // SOLUTION_H
"""

    # Create test.cc
    test_content = f"""#include <gtest/gtest.h>
#include "cpp/{padded_number}/solution.h"

TEST(SolutionTest, Test1) {{
    Solution solution;
    EXPECT_EQ(solution.solution(0), 0);
}}

TEST(SolutionTest, Test2) {{
    Solution solution;
    EXPECT_EQ(solution.solution(1), 0);
}}
"""

    # Write files
    with open(os.path.join(dir_path, "BUILD.bazel"), "w") as f:
        f.write(build_content)

    with open(os.path.join(dir_path, "solution.h"), "w") as f:
        f.write(solution_content)

    with open(os.path.join(dir_path, "test.cc"), "w") as f:
        f.write(test_content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 create_cpp_problem.py <problem_number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        create_problem(number)
        print(f"Created C++ problem {number} successfully!")
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)


if __name__ == "__main__":
    main()
