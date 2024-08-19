class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None )
        def rec (current,clipboard):

            if current  == n:
                return 0 
            if current>n:
                return float("inf")


            res1 = 1+rec(current+clipboard , clipboard) 

            res2  = 2+ rec( 2* current  , current )

            return min(res1 , res2)
        if n ==1 : 
            return 0 
        return 1+ rec(1,1)

        