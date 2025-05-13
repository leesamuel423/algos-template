import java.util.*;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> cache = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int remainder = target - nums[i];
      if (cache.containsKey(remainder)) {
        return new int[]{cache.get(remainder), i};
      } else {
        cache.put(nums[i], i);
      }
    }

    throw new IllegalArgumentException("no solution");
  }
}
