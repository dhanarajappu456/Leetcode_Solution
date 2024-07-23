class Solution:
    def doesAliceWin(self, s: str) -> bool:

        vow  = set(['a','e','i','o','u'])
        cnt  = 0
        for c in s:
            if c in vow:
                cnt+= 1
        return cnt>=1
        