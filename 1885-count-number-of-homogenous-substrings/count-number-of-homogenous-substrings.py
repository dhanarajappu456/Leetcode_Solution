#find length of each homo substring , then number of homosubstring within  a long  homogenous substring   is (n*(n+)1)//2


class Solution:
    def countHomogenous(self, s: str) -> int:
        mod  = 10**9+7
        n  = len(s)
        ans= 0 
        i=0 
        while(i<n): 
            j=i
            while(j<n and s[i]==s[j]):
                j+=1
            length = j-i
            ans += length *(length+1)//2
            i= j
        return ans % mod
            
        