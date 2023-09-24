class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''

        recurive memo solution) 

        starting from the query glass, we go reursively to all possible parents, that fills the current glass, 

        the recursion , will return the amount of champagne that is present in the glass at a time 
        
        since the same champagne might be called again , and the champagne present in a glass not change, so 
        we can memoise it 


        
        '''

        @lru_cache
        def rec(i,j):


            if i==0 and j==0:
                return poured

            if j<0 or j>i:
                return 0
            

            left_par_content = rec (i-1, j-1 )  
            right_par_content =   rec(i-1, j)

            return max(0,left_par_content-1)/2 + max(0,right_par_content-1)/2


        return min(1,rec(query_row, query_glass))
        