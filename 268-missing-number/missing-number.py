class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans= 0 
        n = len(nums)
        ans  = n*(n+1)//2 - sum(nums)
        return ans