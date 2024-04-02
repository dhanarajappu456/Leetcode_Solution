 #solution 3 - tabulation
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod=10**9+7
        dp = [[0 for  j in range(k+1)] for i in range(n+1)]
        for i in range(0,n+1):
            dp[i][0] =1
        for i in range(1,n+1):
            for j in range(1,k+1):
            
                if j<i:
                    ans = (dp[i-1][j]%mod+ dp[i][j-1]%mod)%mod
                else:
                    ans = ans = (dp[i-1][j]%mod+ dp[i][j-1]%mod -dp[i-1][j-i]%mod)%mod
                
                    
                dp[i][j] = ans 
    
        return dp[n][k]
