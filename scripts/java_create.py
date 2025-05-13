#!/usr/bin/env python3
import os
import sys


def create_problem(number):
    # Pad problem number with zeros
    padded_number = str(number).zfill(4)

    # Create directory
    dir_path = f"java/{padded_number}"
    os.makedirs(dir_path, exist_ok=True)

    # Create BUILD.bazel
    build_content = """java_library(
    name = "main",
    srcs = ["Main.java"],
    visibility = ["//visibility:public"],
)

java_test(
    name = "test",
    size = "small",
    srcs = ["MainTest.java"],
    test_class = "MainTest",
    deps = [
      ":main",
      "@maven//:junit_junit"
    ],
)
"""

    # Create Solution.java
    solution_content = """public class Solution {
    public int solution(int input) {
        return 0;
    }
}
"""

    # Create MainTest.java
    test_content = """import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void testSolution() {
    Solution solution = new Solution();

    int[] testCases = {
      0,
      1
    };

    int[] expectedResults = {
      0,
      0
    };

    for (int i = 0; i < testCases.length; i++) {
      int result = solution.solution(testCases[i]);
      assertEquals("Test case " + i + " failed", expectedResults[i], result);
    }
  }
}
"""

    # Write files
    with open(os.path.join(dir_path, "BUILD.bazel"), "w") as f:
        f.write(build_content)

    with open(os.path.join(dir_path, "Solution.java"), "w") as f:
        f.write(solution_content)

    with open(os.path.join(dir_path, "MainTest.java"), "w") as f:
        f.write(test_content)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 create_java_problem.py <problem_number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        create_problem(number)
        print(f"Created Java problem {number} successfully!")
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)


if __name__ == "__main__":
    main()
