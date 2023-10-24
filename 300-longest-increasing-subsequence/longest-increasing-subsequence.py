

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n= len(nums)
        
        #lis ending at each index
        dp = [1 for i in range(n)]
        ans  =1
        i=0
        while(i<n):

            j=i-1
            while(j>-1):
                if nums[j]<nums[i]:
                    
                    dp[i]= max(dp[i], 1+dp[j])

                j-=1
            ans  = max( ans, dp[i])
            i+=1
        print(dp)
        return ans
