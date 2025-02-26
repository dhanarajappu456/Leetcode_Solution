class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        n = len(nums)
        ans  = -float("inf")
        local_pos_max   = -float("inf")
        local_pos_min  = float("inf")
        for i in range(n):
            local_pos_max =  max(local_pos_max + nums[i],  nums[i])
            local_pos_min  = min(local_pos_min   + nums[i] , nums[i] )
            ans = max(ans, local_pos_max, abs(local_pos_min))
        return ans
        




        