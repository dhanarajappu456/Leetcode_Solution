from functools import lru_cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m ,n = len(matrix),len(matrix[0])
        ans = float("inf")
        dir = [(1,0),(1,1),(1,-1)]
        @lru_cache(None)
        def rec(i,j):
            
            if i==m and 0<=j<=n:
                return 0
            elif i>m or j>=n or i<0 or j<0:
                return float("inf")
            ans  = float("inf")
            for dx, dy in dir:

                x,y = i+dx , j+dy
                
                ans = min( ans, matrix[i][j]+ rec(x,y))
            return ans
        
        
        for j in range(n):
                ans = min(ans, rec(0,j))
        return ans 
        