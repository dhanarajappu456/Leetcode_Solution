class Solution {
    public int minimumCost(int[] nums) {
        
        int n = nums.length;
        int[] arr  = Arrays.copyOfRange(nums,1,n);
        Arrays.sort(arr);
        return(nums[0]  + arr[0] + arr[1]);
    }
}