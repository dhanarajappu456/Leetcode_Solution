class Solution {



  private int rec(int i, int j, int[] nums, int[][] memo) {
        if (i > j) {
            return 0;
        }

        if (memo[i][j] != -1) {
            return memo[i][j];
        }

        int maxCoins = 0;
        for (int p = i; p <= j; p++) {
            maxCoins = Math.max(
                maxCoins,
                nums[i - 1] * nums[p] * nums[j + 1] + rec(i, p - 1, nums, memo) + rec(p + 1, j, nums, memo)
            );
        }

        memo[i][j] = maxCoins;
        return maxCoins;
    }
    public int maxCoins(int[] nums) {

      int n = nums.length;
      int m = n+2;
      int[]  paddedNums  = new int[m];
      paddedNums[m-1] = 1;
      paddedNums[0]= 1;
      for(int i=1;i<m-1;i++)
        paddedNums[i] = nums[i-1] ;
      int[][] memo  = new int[m][m];
      for(int[] arr: memo)
        Arrays.fill(arr, -1);
      
    
      return rec(1,m-2,paddedNums, memo);
        
    }
}