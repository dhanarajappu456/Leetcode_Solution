class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        #starting from a cell in an isalnd run dfs and see if all sides of  each cell in island is covered by 1's

        m,n =len(grid), len(grid[0])
        vis = set()
        def rec(i,j):

            if i<0 or i>=m or j<0 or j>=n:
                return False
            
            if( (i,j) in vis )or grid[i][j]==1:
                return True
            
            vis.add((i,j))
            a= rec(i+1,j)  
            b = rec(i,j+1)
            c= rec(i,j-1)
            d = rec(i-1,j)

            return a and b and c and d 
        cnt = 0 
        for i in range(m):
            for j in range(n):

                if ((i,j) not in vis ) and grid[i][j]==0: 
                    if  rec(i,j):
                        cnt+=1
        return cnt

        