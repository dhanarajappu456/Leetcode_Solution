class Solution:
    def longestPalindrome(self, s: str) -> str:


        n = len(s)
        max_len , ans   = 0 ,None
        for i in range(n):
            l,r= i,i 
            while(l>=0 and r<n  and s[l] == s[r]):
                if max_len < ( r-l+1):
                    max_len =  ( r-l+1)
                    ans  = s[l:r+1]
                l-=1
                r+=1
            l,r = i,i+1
            while(l>=0 and r<n  and s[l] == s[r]):
                if max_len < ( r-l+1):
                    max_len =  ( r-l+1)
                    ans  = s[l:r+1]
                l-=1
                r+=1
        return ans


