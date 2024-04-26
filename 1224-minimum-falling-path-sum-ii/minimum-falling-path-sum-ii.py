class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # Initialize the last row of dp with the values of the last row of the grid
        dp[-1] = grid[-1]
        
        # Iterate over the rows from second last to first
        for i in range(n-2, -1, -1):
            # Find the minimum and second minimum value dp[i+1], with their cols also stored
            min1_val,min2_val,min1_col,min2_col = float("inf"),float("inf"),-1,-1
            for j in range(n):
                if dp[i+1][j] <= min1_val:
                    min2_val = min1_val
                    min2_col = min1_col
                    min1_val = dp[i+1][j]
                    min1_col=j
                elif dp[i+1][j] <= min2_val:
                    min2_val = dp[i+1][j]
                    min2_col =j
            
            # Update dp with the minimum falling path sum
            for j in range(n):
                #when we choose grid[i][j] we need to choose min from next row , that is dp[i+1], whose 
                #col!=j 
                dp[i][j] = grid[i][j] + (min1_val if min1_col != j else min2_val)
        
        # The minimum falling path sum will be the minimum value in the first row of dp
        return min(dp[0])
