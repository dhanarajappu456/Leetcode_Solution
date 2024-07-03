import heapq as h 

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        min_4 , max_4  = h.nsmallest(4,nums),h.nlargest(4,nums)
        ans = float("inf")
        for i in range(4):
            ans = min(ans, max_4[3-i]- min_4[i])
        return ans 