class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
    int n = nums.length;

    PriorityQueue<int[]> maxHeap = new PriorityQueue<>((int[] a, int[] b)->{ return b[0]-a[0];});


    int [] dp  = new int[n];

    int ans =Integer.MIN_VALUE;

    for(int i=0 ; i<n;i++){
        int j = i-1 ; 
        dp[i] = nums[i];
        // while(j>=0){

        //     dp[i] = Math.max(dp[i], nums[i]+ dp[j]);
        //     j-=1;
        // }

        while(maxHeap.size()> 0 && i-maxHeap.peek()[1]>k){

                maxHeap.poll();


        }

        if( maxHeap.size()>0){

            dp[i] =Math.max(dp[i], nums[i]+ maxHeap.peek()[0]);
        }
        ans  = Math.max(ans, dp[i]);

        maxHeap.offer(new int[]{dp[i], i});

    }

    return ans ; 
   
    
    
    } 



        
    
}