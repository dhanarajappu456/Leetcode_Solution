
'''

solution 1 - brute - force

go through all the elements and see it col and row  , howmany 1's' and zeros are there in the col and row 

t mn *(m+n)
s  1 

solution 2 - optimised approach

go through all the elements  store num of 1's in each row in a map and num of zeros in each col in a map 
then once again iterate through the grid and fill in the values  using the info in the map

t mn 
s  m+n


'''
#solution2 
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
                #(sum of number of ones in  row and col ) - (sum of number of 0's in row and col)
                grid[i][j] =(ones_row[i]+ones_col[j] )- (n - ones_row[i] + m - ones_col[j])
        return grid
        
        