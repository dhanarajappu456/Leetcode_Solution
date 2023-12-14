from collections import defaultdict as dict
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        ones_row= dict(int)
        ones_col = dict(int)

        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n): 

                if grid[i][j] == 1:
                    ones_row[i]+=1
                    ones_col[j]+=1

    
        for i in range(m):
            for j in range(n):
                grid[i][j] =(ones_row[i]+ones_col[j] )- (n - ones_row[i] + m - ones_col[j])
        return grid
        
        