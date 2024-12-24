class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n,  m = len(s) , len(p)
        if s=="":
            return p.count('*') ==len(p)
        if p =="":
            return False
        dp = [ [False for j in range(m)] for i in range(n)]
        dp[0][0]  =( (p[0] =="*") or (p[0] =="?")  or (p[0] == s[0]))
        
        cnt_non_star = int(p[0].isalpha() or (p[0] =="?")  )
       
        for j in range(1,m):
         
            if p[j]!="*":
                cnt_non_star +=1
            
            if cnt_non_star >1:
                dp[0][j] = False
            
                continue
       
            if p[j].isalpha():
                dp[0][j] =  dp[0][j-1] and (p[j] == s[0])
            else:
                dp[0][j] = dp[0][j-1] and True
      
        for i in range(1,n):

            dp[i][0] = (p[0]== "*" )
        
        for i in range(1,n):
          
            for j in range(1,m):

                if (p[j] =="?") or( p[j]==s[i]):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] =="*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
    
          
        return dp[n-1][m-1]

    