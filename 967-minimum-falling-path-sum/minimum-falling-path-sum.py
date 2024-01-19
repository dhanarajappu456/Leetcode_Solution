'''


solution dp 

t n ^2
s n

'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m ,n = len(matrix),len(matrix[0])
        
        
        prev = [matrix[0][i] for i in range(n)]

        for i in range(1,m):
            curr = [float("inf") for j in range(n)]
            for j in range(n):

                for k in [-1,0,1]:

                    if 0<=j+k<n :
                        curr[j] = min(curr[j], matrix[i][j]+ prev[j+k])
            prev = curr
    
        return  min(prev)
        