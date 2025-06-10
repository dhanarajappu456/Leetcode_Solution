class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid) , len(grid[0])
        
        def dfs(i,j):

            
            if i<0 or i>=m or j>=n or j<0 or (i,j) in vis:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            vis.add((i,j))
            ans = 1 
            ans+= dfs(i+1, j)
            ans+= dfs(i-1, j)
            ans+= dfs(i, j+1)
            ans+= dfs(i, j-1)

            return ans
        
        ans = 0
        vis  = set()
        for i in range(m):
            for j in range(n ):
                if (i,j) not in vis and grid[i][j] ==1:
                    ans = max(ans , dfs(i,j) )
        return ans
                
