from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, val in enumerate(nums):
            remainder = target - val
            if remainder in cache:
                return [cache[remainder], i]
            cache[val] = i
        return [0, 0]
