class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow  = {'a','e','i','o','u'}
        vows = [1 for c in s  if c in vow]
        cnt = sum(vows)
        return cnt>=1
        