class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans  = [ 1 for i in range(n)]
        pref, suff  = 1,1
        for i in range(n):

            ans[i] *=pref
            ans[n-1-i] *= suff
            pref, suff = pref * nums[i] ,suff* nums[n-1-i]

        return ans
  
            