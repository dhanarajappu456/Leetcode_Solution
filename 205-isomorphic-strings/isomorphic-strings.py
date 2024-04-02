class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False
        
        sMap = dict()
        tMap = dict()

        for i,c in enumerate(s):
            
            if c in sMap and sMap[c]!=t[i]:
                return False
            if t[i] in tMap and tMap[t[i]]!=c:
                return False
            sMap[c] = t[i]
            tMap[t[i]] = c
        return True
            
            
            