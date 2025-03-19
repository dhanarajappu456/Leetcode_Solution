class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n  = len(nums)
        cnt = 0 
        for i in range(n):
            if (i >= n-2  )and (nums[i] == 0) :
                return -1
            if(nums[i] == 0):
                nums[i] = 1-nums[i]
                nums[i+1]   = 1 - nums[i+1]
                nums[i+2] =   1-  nums[i+2]
                cnt+=1
            #print(nums)
        return cnt
            

            




            
        