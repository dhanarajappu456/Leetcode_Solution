class Solution:
    def longestPalindrome(self, s: str) -> str:

        S1 ,S2  = s, s[::-1]
        m,n = len(S1) , len(S2)
        dp =[ [ "" for j in range(n+1)] for i in range(m+1)]
        ans = ""

        for i in range(1,m+1):
            
            for j in range(1,n+1):
                
                if S1[i-1] == S2[j-1]:
                    
                    dp[i][j] = dp[i-1][j-1]+S1[i-1]
                    #ans  = max(ans,dp[i][j])
                    if len(dp[i][j])> len(ans) and dp[i][j] ==dp[i][j][::-1]:
                        ans  = dp[i][j]
        return ans
                    
     
                






