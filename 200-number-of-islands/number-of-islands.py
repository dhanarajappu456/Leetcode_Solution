class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):


            #if out of bound return 0
            # if visited return  0 
            if i< 0 or j<0  or i>= m or  j>=n  or (i,j) in vis:
                return 0 
            if grid[i][j] =="0":
                return 0
            ans = 1 
            vis.add((i,j))
            ans += dfs(i+1, j)
            ans += dfs(i-1,j)
            ans += dfs(i,j+1)
            ans += dfs(i, j-1)
            return ans

        
        vis  = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis and grid[i][j] =="1":
                    dfs(i,j)
                    ans +=1 
        return ans

        