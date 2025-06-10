from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        result = []

        def can_reach_both(i, j):
            pacific_reached = atlantic_reached = False
            visited = set()

            def dfs(r, c):
                nonlocal pacific_reached, atlantic_reached
                if (r, c) in visited:
                    return

                if r == 0 or c == 0:
                    pacific_reached = True
                if r == rows - 1 or c == cols - 1:
                    atlantic_reached = True
                if pacific_reached and atlantic_reached:
                    return
                visited.add((r, c))
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[nr][nc] <= heights[r][c]:
                            dfs(nr, nc)
                # Check if we reached Pacific or Atlantic
                

                

                

            dfs(i, j)
            return pacific_reached and atlantic_reached

        for i in range(rows):
            for j in range(cols):
                if can_reach_both(i, j):
                    result.append([i, j])

        return result
