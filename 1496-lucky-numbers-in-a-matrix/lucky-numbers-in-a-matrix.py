class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        m,n = len(matrix),len(matrix[0])
        col_max_min,row_min_max  = float("inf "),float("-inf ")
        for j in range(n):
            max_col = matrix[0][j]
            for i in range(m):
                max_col= max(max_col, matrix[i][j])
            col_max_min = min(col_max_min,max_col) 

        
        for i in range(m):
            row_min  = min(matrix[i])
            row_min_max = max(row_min_max,row_min) 

        return [row_min_max] if row_min_max == col_max_min else []
