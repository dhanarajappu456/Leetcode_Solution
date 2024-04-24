class Solution:
    def tribonacci(self, n: int) -> int:

        @lru_cache(None)
        def rec(n):

            if n==0 :
                return 0 
            if n==1 or n==2 :
                return 1
            
            return rec(n-1) +  rec(n-2) + rec(n-3)
        return rec(n)