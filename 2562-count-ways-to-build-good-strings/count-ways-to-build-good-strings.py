

from collections import defaultdict as dict 
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9+7
        # @lru_cache(None)
        # def rec(length):

        #     if length >high: 
        #         return 0
            
        #     ans =(rec(length+zero)%mod + rec(length+one)%mod)%mod
        #     ''' we increment count for each string that has length with in range >=low and <=high '''
        #     if length>=low:
        #          return( 1+ ans)%mod
        #     else:
        #         return ans 
        # return rec(0)

        dp =[0 for i in range(high+1)]
        for length in range(high,-1,-1):

            ans = 0 
            if length+zero <=high:
                ans  = (ans%mod + (dp[length+zero])%mod)%mod
            if length+one <=high:
                ans =( ans%mod + dp[length+one]%mod)%mod

            if length>=low:
                ans = (1+ans%mod)%mod
            dp[length] =  ans 
        return dp[0]
