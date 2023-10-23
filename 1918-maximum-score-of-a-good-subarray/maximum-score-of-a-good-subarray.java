class Solution {
    public int maximumScore(int[] nums, int k) {


        //  '''

        //     find the index of prevsmall and next small number  for each number 

        //     then iterate on the nums array , and each num as minimum of the  subarray and score  and also including k 
        //     find the score and store max score

        // '''


    int n = nums.length;
    int[] prevSmall = new int[n];
    int [] nextSmall = new int[n];
    
    Stack<int[]> stk = new Stack<int[]>();
    stk.push(new int[]{-1,-1});
        for(int  i = 0 ;i<nums.length ;i++){

            int num  = nums[i];
            while(!stk.empty() && stk.peek()[1]>= num){


                stk.pop();
            }
            
            prevSmall[i] = stk.peek()[0];
            stk.push(new int[]{i,num});

        }
            
        stk.clear();
        stk.push(new int[]{n,-1});
        for(int i= nums.length-1;i>=0 ; i--){

            int num  = nums[i];
            
            while(!stk.empty()  && stk.peek()[1]>= num){
                stk.pop();
            

            }
              
            nextSmall[i] = stk.peek()[0];
            stk.push(new int[]{i,num});
        }
            
        int  ans =  nums[k];
        for(int p = 0; p<nums.length;p++){
            int num  = nums[ p];
            int i = prevSmall[p]+1;
            int j = nextSmall[p]-1;
            //if the subarray is good subarray , take the score into accounte 
            if (i<=k && k<=j){
                ans =Math.max(ans, num *(j-i+1));

            }
        }
               
        return ans;
    

}
}