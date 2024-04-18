class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:



        def dfs(i,j,visited):

            if len(grid)<=i or i<0 or len(grid[0])<=j or j<0 or grid[i][j]==0:
                return 1
            elif (i,j) in visited :
                return 0

            visited.add((i,j))
            return(
            dfs(i-1,j,visited)+
            dfs(i,j+1,visited)+
            dfs(i+1,j,visited)+
            dfs(i,j-1,visited)
            )
                
            

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j,visited)
    

        