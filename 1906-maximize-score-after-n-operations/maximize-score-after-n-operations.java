import java.util.HashMap;
import java.util.Map;

class Solution {
    private int gcd(int a, int b) {
        if (a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }

    private int rec(int i, int mask, int[] nums, Map<String, Integer> memo) {
        if (mask == 0) {
            return 0;
        }
      
        String key = i + "-" + mask;
        
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int ans = 0;
        int n = nums.length;
        for (int j = 0; j < n - 1; j++) {
            if (((1 << j) & mask) != 0) {
                for (int k = j + 1; k < n; k++) {
                    if (((1 << k) & mask) != 0) {
                        int newMask = mask & ~(1 << j);
                        newMask = newMask & ~(1 << k);
                        ans = Math.max(ans, i * gcd(nums[j], nums[k]) + rec(i + 1, newMask, nums, memo));
                    }
                }
            }
        }

        memo.put(key, ans);
        return ans;
    }

    public int maxScore(int[] nums) {
        int n = nums.length;
        int mask = (1 << n) - 1; // Initialize mask properly
        Map<String, Integer> memo = new HashMap<String,Integer>();
        return rec(1, mask, nums, memo);
    }
}
