class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0 
        for i in range(n):
            min_,max_ = nums[i],nums[i]
            for j in range(i,-1,-1):
                min_,max_ = min(min_,nums[j]),max(max_,nums[j])
                ans += (max_ - min_)
        return ans

        