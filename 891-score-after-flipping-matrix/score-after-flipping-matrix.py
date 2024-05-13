class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        col_size=len(grid[0])
        row_size=len(grid)
        mask=(1<<col_size)-1
        for i in range(row_size):
            val=0
            for j in grid[i]:
                val<<=1
                val|=j
            if(val^mask>val):
                for j in range(col_size):
                    grid[i][j] = grid[i][j] ^ 1
        #print(grid)            
        for j in range(col_size):
            count_zero=0
            count_one=0
            for k in range(row_size):
                if(grid[k][j]==0):
                    count_zero+=1
                else:
                    count_one+=1
            if(count_zero>count_one):
                for i in range(row_size):
                    grid[i][j] = grid[i][j] ^ 1
        sum_=0
        for i in grid:
            cnt=1
            for j in i:
                sum_+=(2**(col_size-cnt))*j
                cnt+=1   
        return sum_             
                    
                    
            
                
            
        