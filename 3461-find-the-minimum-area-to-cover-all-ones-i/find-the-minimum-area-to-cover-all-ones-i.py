class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n  = len(grid) , len(grid[0])
        first_row , last_row, first_col , last_col = m-1 ,0, n-1, 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    first_row = min(first_row, i)
                    first_col = min(first_col, j)
                    last_row = max(last_row, i)
                    last_col = max(last_col, j)
        return((last_row - first_row +1 ) * (last_col - first_col+1))
        
                    



