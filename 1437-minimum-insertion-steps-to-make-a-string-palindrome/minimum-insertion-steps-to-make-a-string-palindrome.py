class Solution:
    def minInsertions(self, s: str) -> int:


        rev= s[::-1]
        m,n  = len(s) ,len(s)
        
        prev = [0 for j in range(n+1)]
        curr=  [0 for j in range(n+1)]

        for i in range(1,m+1):
            curr=  [0 for j in range(n+1)]
            for  j in range(1,n+1):

                if s[i-1] == rev[j-1]:

                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] =max(prev[j] , curr[j-1])
            prev  = curr
   
        return (len(s) - prev[m])