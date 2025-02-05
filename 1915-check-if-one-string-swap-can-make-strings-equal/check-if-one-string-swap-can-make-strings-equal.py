from collections import defaultdict as dict

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mp = dict(int)
        miss  =  0

        for c in s2:
            mp[c]+=1
   
        for i,c in enumerate(s1):
            mp[c]-=1
            if mp[c] == 0:
                mp.pop(c)
            
            if c != s2[i]:
                miss+=1
     
        return (len(mp) == 0) and (miss<=2)