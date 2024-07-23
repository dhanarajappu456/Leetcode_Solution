# Sorry Bob\U0001f614\U0001f614

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow  = {'a','e','i','o','u'}
        vows = [1 for c in s  if c in vow]
        cnt = sum(vows)
        return cnt>=1
        