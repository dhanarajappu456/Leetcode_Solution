

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mp =[ 0 for i in range(26)]
        mod = 10**9+7
        for c  in s:
            mp[ord(c)-97]+=1
        for i in range(t):
            temp = [0 for i in range(26)]
            for k in  range(26):
               
                if k == 25:
                    cnt = mp[k]
                    #character a 
                    temp[0]  += cnt
                    #character  b  
                    temp[1]  += cnt
                else:
                    cnt = mp[k]
                    # next character
                    temp[k+1] = temp[k+1] + cnt
            mp = temp
        ans = 0 
        for i in range(26):
            ans = (ans + mp[i]%mod)%mod
        return ans






        