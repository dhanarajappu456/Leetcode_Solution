class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # Initialize the last row of dp with the values of the last row of the grid
        dp[-1] = grid[-1]
        
        # Iterate over the rows from second last to first
        for i in range(n-2, -1, -1):
            # Find the minimum and second minimum value in the current row
            min_val, second_min_val = float('inf'), float('inf')
            for j in range(n):
                if dp[i+1][j] < min_val:
                    second_min_val = min_val
                    min_val = dp[i+1][j]
                elif dp[i+1][j] < second_min_val:
                    second_min_val = dp[i+1][j]
            
            # Update dp with the minimum falling path sum
            for j in range(n):
                dp[i][j] = grid[i][j] + (min_val if dp[i+1][j] != min_val else second_min_val)
        
        # The minimum falling path sum will be the minimum value in the first row of dp
        return min(dp[0])
