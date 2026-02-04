class Solution {
    public int maxSubArray(int[] nums) {
            int ans = Integer.MIN_VALUE;
        int local_ = 0;
        
        for (int num : nums) {
            local_ = Math.max(num, local_ + num);
            ans = Math.max(local_, ans);
        }
        
        return ans;
    }
}