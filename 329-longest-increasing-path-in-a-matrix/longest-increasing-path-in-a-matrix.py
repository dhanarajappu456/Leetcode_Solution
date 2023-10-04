from functools import lru_cache
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        m,n   = len(matrix) ,len(matrix[0])


        def out(i,j):

            if( 0<=i<=m-1) and (0<=j<=n-1):
                return False
            return True



        @lru_cache(None)
        def dfs(i,j):

            if out(i,j):
                return 0

            ans=1
            if (not out(i+1,j)) and( matrix[i+1][j] > matrix[i][j]):
                print(i,j)
                ans = max(ans, 1+dfs(i+1,j))
            if (not out(i,j+1)) and( matrix[i][j+1] > matrix[i][j]):
          
                ans = max(ans, 1+dfs(i,j+1))
            
            
            
            if (not out(i-1,j)) and( matrix[i-1][j] > matrix[i][j]):
          
                ans = max(ans, 1+dfs(i-1,j))
            
            if (not out(i,j-1)) and( matrix[i][j-1] > matrix[i][j]):
          
                ans = max(ans, 1+dfs(i,j-1))
            return ans 
        

        ans = -1
        for i in range(m):

            for j in range(n):

                ans = max(ans , dfs(i,j)) 
        return ans


    
        