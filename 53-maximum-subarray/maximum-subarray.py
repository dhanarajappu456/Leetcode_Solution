class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        local_ = 0
        for num in nums:
            local_ = max(num,  local_+ num)
            ans  = max(local_, ans)
        return ans