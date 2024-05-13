class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        col_size=len(grid[0])
        row_size=len(grid)
        mask=(1<<col_size)-1
        #flipping the row if possible
        for i in range(row_size):
            val=0
            for j in grid[i]:
                val<<=1
                val|=j
            if(val^mask>val):
                for j in range(col_size):
                    grid[i][j] = grid[i][j] ^ 1
        #flipping the col if possible 
        for j in range(col_size):
            count_one=0
            for i in range(row_size):
                count_one += (grid[i][j] & 1 )
            count_zero  = row_size - count_one
            if( count_zero >count_one):
                for i in range(row_size):
                    grid[i][j] = grid[i][j] ^ 1
        #finding the sum
        sum_=0
        for i in grid:
            ans = 0
            for j in i:
                ans = (ans << 1)  + j
            sum_ += ans
        return sum_             
                    
                    
            
                
            
        