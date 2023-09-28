from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the size of the grid
        m, n = len(grid), len(grid[0])
        
        # Initialize the dp table with the same dimensions as the grid
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Set the starting value
        dp[0][0] = grid[0][0]
        
        # Initialize the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Initialize the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill the dp table
        for i in range(1, m):
            for j in range(1, n):
                # The value at dp[i][j] is the value at grid[i][j] plus the minimum of the values
                # to its left and above
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]

