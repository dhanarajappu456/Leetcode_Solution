class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n  = len(mat),len(mat[0])
        def check_special(i,j):
            for r in range(m):
                if mat[r][j] and r!=i:
                    return False
            for c in range(n):
                if mat[i][c] and c!=j:
                    return False
           
            return True

        ans =0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1: 
                    if check_special(i,j):
                        ans+=1
        return ans 


        