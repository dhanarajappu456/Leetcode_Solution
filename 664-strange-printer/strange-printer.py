class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def rec(i,j):

            if i>j:
                return float("inf")
            if i==j:
                return 1

            print(i,j)
            min_ =float("inf")
            for k in range(i,j):

                min_  = min(min_, rec(i,k)  + rec(k+1,j))

            return min_-1  if s[i] == s[j] else min_
    
        return rec(0,n-1)