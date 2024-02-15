class Solution {
    public long largestPerimeter(int[] nums) {
        
        
         Arrays.sort(nums);
        int n = nums.length;
        long [] pref = new long[n];
        
        pref[0] = nums[0];
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + nums[i];
        }
        int ans = -1;
        for (int i = n - 1; i >= 2; i--) {
            int longest = nums[i];
            if (pref[i - 1] > longest) {
                return pref[i - 1] + longest;
            }
        }
        return ans;
        
    }
    
    
}