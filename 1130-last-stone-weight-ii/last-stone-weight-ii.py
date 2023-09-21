#this is variatoin of Minimum Difference Subsets! https://www.interviewbit.com/problems/minimum-difference-subsets/
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        nums = stones
        tot_sum = sum(stones)
        n =len(stones)
        memo = {}

        target  = sum(nums)//2
        def rec(ind, sum_):

            if sum_ >= target or ind ==n :
                return abs(tot_sum - 2*sum_)
            if (ind, sum_) in memo:
                return memo[(ind,sum_)]
            tk = rec( ind+ 1, sum_+nums[ind])
            not_ = rec(ind+1, sum_)
            memo[(ind, sum_)] = min(tk,not_)
            return memo[(ind, sum_)]
        return rec(0, 0)