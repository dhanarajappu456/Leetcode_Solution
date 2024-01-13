class Solution:
    def minSteps(self, s: str, t: str) -> int:
        

        tmap = dict()
        smap = dict()

        for c in  t:
            tmap[c] = tmap.get(c,0)+1
        ans = 0 
        for c in  s:
            smap[c] = smap.get(c,0)+1
            if smap[c]> tmap.get(c,0):
                ans +=1
            
        return ans