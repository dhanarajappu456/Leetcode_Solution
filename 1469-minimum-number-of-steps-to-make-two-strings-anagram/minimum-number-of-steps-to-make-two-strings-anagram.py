'''
greedy using map 

to find the min number of chars to replace in s, 
we need to find the max nuber of chars in s that already match with that of the chars in t

for missing chars in s , we incremenet the ans , finally giving the required ans

t n 
s  n

'''

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