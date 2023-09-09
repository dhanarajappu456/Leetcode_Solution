class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        #tabulation
        n = len(nums)


        dp = [-1 for i in range(target+1)]
        dp[0] = 1

        for sum_ in range(1,target+1):
            ans = 0 
            for num in (nums):
                if sum_-num>=0:
                    ans+= dp[sum_-num]
            dp[sum_] = ans
        return dp[target]






        # memo  ={}
        # def rec(sum_):

        #     if sum_<=0:

        #         return 1 if sum_== 0  else 0
        #     if sum_ in memo:
        #         return memo[sum_]
        #     ans = 0 

        #     for num in (nums):

        #         ans+= rec(sum_-num)
        #     memo[sum_] = ans

        #     return memo[sum_] 
        # return rec(target)