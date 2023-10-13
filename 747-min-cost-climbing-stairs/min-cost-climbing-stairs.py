class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        nums = cost
        n = len(cost)
        @lru_cache(None)
        def rec(ind):
            if ind >= n+1:
                return 0
            if ind  ==0:
                ans = min(rec(ind+1) , rec(ind+2))
            else:

                ans  = min(nums[ind-1]+ rec(ind+1) , nums[ind-1]+rec(ind+2))
            return ans

        return rec(0)
