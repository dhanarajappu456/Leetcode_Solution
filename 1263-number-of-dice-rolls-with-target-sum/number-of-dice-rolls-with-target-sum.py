#solution 1 
'''

this is simple recursive memo solution for the problem 
the state (n, tar)-> denote the 
number of ways we can get the tar with remaining dice roll , which is overlapping subproblem 
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = 10**9+7
        # @lru_cache(None)
        # def rec(n,tar):
            
            
        #     if n ==  0:
        #         return int(tar==0)
        #     if tar<0:
        #         return 0
        #     ans = 0
        #     for i in range(1,k+1):
        #         ans = (ans%mod + rec(n-1, tar-i)%mod)%mod
        #     return ans

        # return rec(n,target)


    
    
        dp =[[0 for i in range(target+1)] for  j in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(1,target+1):
                ans = 0
                for f  in range(1,k+1):
                    if j-f>=0:
                        if i==2 and j==2:
                            print(i-1,j-f,dp[i-1][j-f])
                        ans = (ans%mod + dp[i-1][j-f]%mod)%mod
                dp[i][j]= ans 

        return dp[n][target]




