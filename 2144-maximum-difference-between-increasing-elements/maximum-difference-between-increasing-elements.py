class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        

        min_ = nums[0]
        ans = -1
        n  = len(nums)
        for i in range(1,n):
            if nums[i]> min_:
                ans = max(ans , nums[i] -  min_)
            min_  = min(min_ , nums[i])
        return ans


            