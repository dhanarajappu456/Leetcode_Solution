from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific Ocean (top row and left column)
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])

        # Start DFS from Atlantic Ocean (bottom row and right column)
        for i in range(rows):
            dfs(i, cols - 1, atlantic, heights[i][cols - 1])
        for j in range(cols):
            dfs(rows - 1, j, atlantic, heights[rows - 1][j])

        # Find all cells that can reach both oceans
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result
