class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        # i = 0
        # j = 0
        # cnt = 0 
        # while(i<n):
           
        #     while(j<n and ((nums[j]-nums[i])<=k)):
        #         j+=1
        #     cnt+=1
        #     i = j
        # return cnt 


        ans  = 1 
        min_val = nums[0]
     
        for i in range(1,n):
            if((nums[i] - min_val) > k):
                ans += 1
                min_val  = nums[i]
        return ans
        