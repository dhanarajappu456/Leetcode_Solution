class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        ans  = 0
        d =  {0:-1}
        n  = len(nums)
        prefixSum = 0
        for i in range(n):
            
            
            
            if nums[i]==1:
                val = 1
            else:
                val = -1
            
            prefixSum  = prefixSum +val
            if prefixSum in d:
                
                ans =max(ans, i-d[prefixSum])
            else:
                d[prefixSum]= i
                
        return ans
        