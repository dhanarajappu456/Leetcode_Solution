class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:


        glass  = [ [ 0 for j in range(i+1)] for i in range(query_row+1) ]

        glass[0][0] = poured


        for i in range(1, query_row+1):

            for j in range(i+1):

                #receive the champagne from the 2 parents
                left_liq , right_liq = 0,0
                if 0<=j-1:

                    left_liq = glass[i-1][j-1]

                if j<i:
                    print(i,j)
                    right_liq = glass[i-1][j]
                
                glass[i][ j ] = max(0, left_liq -1 )*0.5  + max(0, right_liq -1 )*0.5 
   

        return min(1,glass[query_row][query_glass] )
        