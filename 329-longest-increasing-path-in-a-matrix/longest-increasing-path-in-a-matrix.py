from functools import lru_cache
class Solution(object):

    '''
    the idea is simple we try starting from each cell , what is the longest Increasing path 

    you can do this in two ways

    1) with the state ( i,j ,prevalue)
    2) with out using prevValue passed to next call , ie, state = (i,j)

    in current call we make sure next call is made iff adjacent cell is greater than the current cell-(this is the way we did below)

    '''
    def longestIncreasingPath(self, matrix):
       
        m,n   = len(matrix) ,len(matrix[0])


        def out(i,j):

            if( 0<=i<=m-1) and (0<=j<=n-1):
                return False
            return True



        memo  = {}


        def dfs(i,j):

            if out(i,j):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            ans=1
            if (not out(i+1,j)) and( matrix[i+1][j] > matrix[i][j]):
       
                ans = max(ans, 1+dfs(i+1,j))
            if (not out(i,j+1)) and( matrix[i][j+1] > matrix[i][j]):
          
                ans = max(ans, 1+dfs(i,j+1))
            
            if (not out(i-1,j)) and( matrix[i-1][j] > matrix[i][j]):
          
                ans = max(ans, 1+dfs(i-1,j))
            
            if (not out(i,j-1)) and( matrix[i][j-1] > matrix[i][j]):
          
                ans = max(ans, 1+dfs(i,j-1))
            
            memo[(i,j)]= ans

            return memo[(i,j)]
        

        ans = 0
        for i in range(m):

            for j in range(n):

                ans = max(ans , dfs(i,j)) 
        return ans


    
        