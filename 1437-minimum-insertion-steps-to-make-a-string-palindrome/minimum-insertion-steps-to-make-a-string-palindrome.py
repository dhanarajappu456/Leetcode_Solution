class Solution:
    def minInsertions(self, s: str) -> int:


        rev= s[::-1]
        m,n  = len(s) ,len(s)
        
        dp = [[0 for j in range(n+1)] for i  in range(m+1)]

        for i in range(1,m+1):
            for  j in range(1,n+1):

                if s[i-1] == rev[j-1]:

                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] =max(dp[i-1][j] , dp[i][j-1])
        return (len(s) - dp[m][n])