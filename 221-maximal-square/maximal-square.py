
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m,n  = len(matrix) , len(matrix[0])
        def outBound(i,j):
            return i<0 or j<0 or i>=m or j>=n 
        @lru_cache(None)
        def rec(i,j):
            if outBound(i,j) or matrix[i][j] =="0":
                return 0 
 
            ans = 0 
            if matrix[i][j] =="1":

                ans= 1+min(rec(i+1, j+1),
                rec(i,j+1),
                rec(i+1, j))
            
            return ans

        
        ans  = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":

                    ans  = max( ans, rec(i,j)) 
        return ans**2



    
        