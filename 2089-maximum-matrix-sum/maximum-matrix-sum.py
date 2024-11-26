class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        nums =  matrix
        m  = len(matrix)
        n = len(matrix[0])
        total = 0
        row_neg_counts = 0
        col_neg = 0
        min_abs = abs(nums[0][0])
        for i in range(m):
            row_neg_counts = 0
            for j in range(n):
                total+= abs(nums[i][j])
                min_abs = min(abs(nums[i][j]),min_abs)
                if nums[i][j]  <0:
                    row_neg_counts+=1
            col_neg += (row_neg_counts%2)
        if col_neg %2 ==1:
            total -= 2*min_abs
        return total


        