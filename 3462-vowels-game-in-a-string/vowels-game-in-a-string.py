class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow  = set(['a','e','i','o','u'])
        cnt  = 0
        vows = [1 for c in s  if c in vow]
        cnt = sum(vows)
        return cnt>=1
        