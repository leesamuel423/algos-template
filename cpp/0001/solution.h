#ifndef SOLUTION_H
#define SOLUTION_H

#include <iostream>
#include <map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::map<int, int> cache;

    for (int i = 0; i < nums.size(); i++) {
      const int remainder = target - nums[i];
      if (cache.find(remainder) != cache.end()) {
        return {cache[remainder], i};
      } else {
        cache[nums[i]] = i;
      }
    }

    return {-1};
  }
};

#endif // SOLUTION_H
