class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dir_ = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        vis = set()
        def dfs(i,j):
            if i<0 or j<0 or i>=m  or j>=n or  ((i,j ) in vis ) or grid[i][j] == 0:
                return 0 
            ans  = grid[i][j]
            vis.add((i,j))
            for d in dir_:
                x,y =  i+d[0] , j+d[1]
                ans  = ans  + dfs(x,y)
            return ans
        res  = 0
        for i in range(m):
            for j in range(n):
                if (i,j)  not in vis and grid[i][j] > 0:
      
                    res = max(res , dfs(i,j))
        return res
            