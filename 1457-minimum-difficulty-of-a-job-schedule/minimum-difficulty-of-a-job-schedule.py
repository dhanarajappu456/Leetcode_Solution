from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs  = jobDifficulty
        n = len(jobs)

        if d>n:
            return -1

        @lru_cache(None)
        def  rec(i,d):
           
            if i ==n:

                return 0 if d==0 else  float("inf")
            
            if d==0:
                return float("inf")

            ans  = float("inf")
            max_diff = -1
            for j in range(i,n):

                max_diff  = max ( max_diff, jobs[j])
                ans = min(ans, max_diff + rec(j+1,d-1))
            return ans

        return rec(0,d)



            



        