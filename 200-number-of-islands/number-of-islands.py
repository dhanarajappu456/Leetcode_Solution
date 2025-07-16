class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid ),  len(grid[0])
        vis  = set()
        def out(i,j):
            return i<0 or j<0 or i>=m  or j>=n

        def dfs(i,j):
            if out(i,j) or ((i,j) in vis ) or grid[i][j] =="0":
                return
            vis.add((i,j))
            dfs(i+1, j)
            dfs(i,j+1)
            dfs(i-1, j)
            dfs(i,j-1)
        cnt  = 0 
        for i in range(m):
            for j in range(n):
                if  (i,j)   not in vis  and grid[i][j] == "1":
                    cnt+=1
                    dfs(i,j)
        return cnt

        