


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

                
        def is_magic(grid, r, c):
            # A 3x3 grid starting at (r, c) must contain distinct numbers from 1 to 9
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)
            
            # Check sums for rows, columns, and diagonals
            s = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != s:
                return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != s:
                return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != s:
                return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
           
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(grid, r, c):
                    count += 1
        
        return count



        
        