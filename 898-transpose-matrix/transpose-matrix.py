

'''
The value in transpose matrix  trans[i][j] is the value at matrix[j][i]
t mn
s mn
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        trans = [[ 0 for j in range(m)] for i in range(n)]


        for i in range(n):
            for j in range(m):
                trans[i][j] = matrix[j][i]
        return trans

        