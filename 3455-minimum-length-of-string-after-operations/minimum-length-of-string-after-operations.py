from collections import defaultdict as dict

class Solution:
    def minimumLength(self, s: str) -> int:
        d= dict(int)
        
        n = len(s)
        min_len = n
        for i in range(n):
            c  = s[i]
            d[c]+=1
            if d[c] == 3:
                min_len -=2
                d[c]=1
        return min_len
