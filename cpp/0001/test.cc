#include "cpp/0001/solution.h"
#include <gtest/gtest.h>

TEST(TwoSum, Test1) {
  Solution solution;
  std::vector<int> nums = {2, 7, 11, 15};
  std::vector<int> expected = {0, 1};
  EXPECT_EQ(solution.twoSum(nums, 9), expected);
}

TEST(TwoSum, Test2) {
  Solution solution;
  std::vector<int> nums = {3, 2, 4};
  std::vector<int> expected = {1, 2};
  EXPECT_EQ(solution.twoSum(nums, 6), expected);
}

TEST(TwoSum, Test3) {
  Solution solution;
  std::vector<int> nums = {3, 3};
  std::vector<int> expected = {0, 1};
  EXPECT_EQ(solution.twoSum(nums, 6), expected);
}
