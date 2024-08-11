class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m,n  = len(grid), len(grid[0])

        def dfs(r,c,visit):
            if (r<0) or (c<0 ) or ( r>=m ) or (c>=n ) or ((r,c)  in visit) or (grid[r][c]==0):
                return 
            visit.add((r,c))
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)

        def count_island(visit):
            island  = 0 
        
            for r in range(m):
                for c in range(n):
                    if ((r,c) not in visit ) and grid[r][c] ==1:
                        dfs(r,c,visit)
                        island += 1
            return island
        vist = set()
        island =count_island(vist) 
     
        if (island  == 0) or (island >1  ):
            return 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] ==1:
                    grid[r][c] = 0
                    visit = set()
                    island =count_island(visit) 
                    if island !=1 :
                        return 1 
                    grid[r][c] = 1
        

        return 2

        
        