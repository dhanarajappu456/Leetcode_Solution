class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''

        simulate the pouring 

        we conatruct  2d array representing the glass, 

        now four a glass at (i,j) it can receive the champagne , from two parents, one at (i-1,j-1) , and other at (i-1, j),
        also  remember, when a glass receive the champagne , from the  parent, it receive the a qunatitiy ,  after the parent took 1 glass, and , which is split into half 
        '''

        glass  = [ [ 0 for j in range(i+1)] for i in range(query_row+1) ]

        glass[0][0] = poured


        for i in range(1, query_row+1):

            for j in range(i+1):

                #receive the champagne from the 2 parents
                left_liq , right_liq = 0,0
                if 0<=j-1:

                    left_liq = glass[i-1][j-1]

                if j<i:
           
                    right_liq = glass[i-1][j]
            
                glass[i][ j ] = max(0, left_liq -1 )*0.5  + max(0, right_liq -1 )*0.5 
   
        
        #remember, the qunatity of champagne at any glass, can't be more than 1 , no matter how much we poured from the above
        

        return min(1,glass[query_row][query_glass] )
        