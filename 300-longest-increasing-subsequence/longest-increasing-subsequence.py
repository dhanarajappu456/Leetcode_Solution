

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n= len(nums)
        
      
        dp =[[0 for j in range(n+1)] for i in range(n+1)]
        
        for ind in range(n-1, -1,-1):
            for preInd in range(0,ind+1):
                take= float("-inf")
                if preInd== 0 or nums[ind]>nums[preInd-1]:
                    take   = 1+ dp[ind+1][ind+1]
                notTake = dp[ind+1][preInd]
                dp[ind][preInd] =  max(take,notTake)
        return dp[0][0]
