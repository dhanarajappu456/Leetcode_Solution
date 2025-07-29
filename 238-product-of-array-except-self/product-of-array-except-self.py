class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = 1 
        ans  = [ 0  for i in range(n)] 
        suf =  [0  for i in range(n)] 
        
        for i,num in enumerate(nums): 
            ans[i] = pref
            pref*= num
        suff = 1 
        for i in range(n-1,-1,-1):
            ans[i]*=suff 
            suff*= nums[i]
        return ans
  
            