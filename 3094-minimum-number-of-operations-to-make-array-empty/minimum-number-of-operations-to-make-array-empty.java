import java.util.HashMap;
import java.util.Map;
import java.lang.Math;

public class Solution {
    public int minOperations(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        int ans = 0;

        for (int num : nums) {
            m.put(num, m.getOrDefault(num, 0) + 1);
        }

        for (int num : m.keySet()) {
            if (m.get(num) == 1) {
                return -1;
            } else {
                ans += Math.ceil( m.get(num) / 3.0);
            }
        }

        return ans;
    }
}
