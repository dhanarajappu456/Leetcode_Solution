#find length of each homo substring , then number of homosubstring within  a long  homogenous substring   is (n*(n+)1)//2


class Solution:
    def countHomogenous(self, s: str) -> int:
        mod  = 10**9+7
        n  = len(s)
        ans= 0 
        for i in range(n):
            
            if i>0 and s[i]==s[i-1]:
                length+=1
            
            else:
                length = 1 
            

            ans+= length
        
        return ans%mod
        