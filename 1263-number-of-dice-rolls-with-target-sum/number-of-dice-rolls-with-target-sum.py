#solution 1 
'''

this is simple recursive memo solution for the problem 
the state (n, tar)-> denote the 
number of ways we can get the tar with remaining dice roll , which is overlapping subproblem 
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = 10**9+7
        @lru_cache(None)
        def rec(n,tar):
            
            
            if n ==  0:
                return int(tar==0)
            if tar<0:
                return 0
            ans = 0
            for i in range(1,k+1):
                ans = (ans%mod + rec(n-1, tar-i)%mod)%mod
            return ans

        return rec(n,target)