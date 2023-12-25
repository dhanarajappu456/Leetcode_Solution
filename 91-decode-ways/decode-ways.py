class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp =[0 for i in range(n+1)] 
        dp[n]=1
        for i in range(n-1,-1,-1):
            ans = 0
            if s[i]=='0':
                continue 
            else:

                for j in range(i,min(i+2,n)):
                    if int(s[i:j+1])<=26:
                    
                        ans+= dp[j+1]
            dp[i] = ans
        return dp[0]
