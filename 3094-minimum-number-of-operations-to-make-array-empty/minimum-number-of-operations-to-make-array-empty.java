import java.util.HashMap;
import java.util.Map;

public class Solution {
    private Map<Integer, Integer>  memo = new HashMap<>();
    private Map<Integer, Integer> m = new HashMap<>();

    public int minOperations(int[] nums) {
       
        
        int ans = 0;

        for (int num : nums) {
            m.put(num, m.getOrDefault(num, 0) + 1);
        }

        for (int num : m.keySet()) {
            int minOp = dfs(m.get(num));
            if (minOp == Integer.MAX_VALUE) {
                return -1;
            }
            ans += minOp;
        }

        return ans;
    }

    private int dfs(int count) {
        if (count == 0) {
            return 0;
        }
        if (count == 1) {
            return Integer.MAX_VALUE;
        } else if (count == 2) {
            return 1;
        } else {
            if (memo.containsKey(count)) {
                return memo.get(count);
            }

            int result = 1 + Math.min(dfs(count - 2), dfs(count - 3));
            memo.put(count, result);
            return result;
        }
    }
}
