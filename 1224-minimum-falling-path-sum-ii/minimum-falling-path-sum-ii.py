'''

solution 2 - dp solution


the dp solution fo solution 1 

t n^3
s n

'''

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0 for i in range(n+1)] for i in range(n+1)]
  
        #state indicate the min sum when choosing element from ith row to 
        #end row , with j-1 being the column chosen from the previous row
        for i in range(n-1,-1,-1):
            #     j-1 being the previous index chosen
            for j in range(n+1):
                m  = float("inf")
                for c in range(n):
                    if c!=j-1:
                        m = min(m  ,grid[i][c]+ dp[i+1][c+1])
                
                dp[i][j]= m 

        return min(dp[0])


        