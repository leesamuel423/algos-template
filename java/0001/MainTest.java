import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

  @Test
  public void testTwoSum() {
    Solution solution = new Solution();

    int[][] testCasesNums = {
      {2, 7, 11, 15},
      {3, 2, 4},
      {3, 3},
    };
    int[] testCasesTargets = {
      9,
      6,
      6
    };

    int[][] expectedResults = {
      {0, 1},
      {1, 2},
      {0, 1},
    };

    for (int i = 0; i < testCasesNums.length; i++) {
      int[] result = solution.twoSum(testCasesNums[i], testCasesTargets[i]);
      assertArrayEquals("Test case " + i + " failed", expectedResults[i], result);
    }
  }
}
