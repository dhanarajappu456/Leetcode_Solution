class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        nums = stones
        tot_sum = sum(stones)
        n =len(stones)
        memo = {}


        def rec(ind, sum_):

            if ind ==n :
                return abs(tot_sum - 2*sum_)


            if (ind, sum_) in memo:
                return memo[(ind,sum_)]
            tk = rec( ind+ 1, sum_+nums[ind])
            not_ = rec(ind+1, sum_)
            memo[(ind, sum_)] = min(tk,not_)
            return memo[(ind, sum_)]
        return rec(0, 0)