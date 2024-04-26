class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        @lru_cache(None)
        def rec(i,j):
            m = float("inf")

            if i == n:
                return 0
            for c in range(n):
                if c!=j:
                    m = min(m  ,grid[i][c]+ rec(i+1,c))
            
            return m
        return rec(0,-1)


        