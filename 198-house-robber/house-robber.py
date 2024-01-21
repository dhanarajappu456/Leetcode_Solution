class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo  =  {}
        def rec(ind):

            if ind >=n :
                return 0 
            if ind in memo:
                return memo[ind]

            tk,not_ = nums[ind]+ rec(ind+2) , rec(ind+1)

            memo[ind] =  max(tk,not_)
            return memo[ind]
        return rec(0)