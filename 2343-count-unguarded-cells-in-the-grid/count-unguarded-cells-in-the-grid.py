class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        mat = [[0 for j in range(n)] for i in range(m)]

        for a,b in walls:
            mat[a][b] = 2
        for a,b in guards:
            mat[a][b] = 1
        def mark_guarded(a,b):

            for r in range(a-1,-1,-1):
                if mat[r][b] in [1,2]:
                    break
                mat[r][b]  = 3
            for r in range(a+1,m):
                if mat[r][b] in [1,2]:
                    break
                mat[r][b] = 3 
            
            for c in range(b-1,-1,-1):
                if mat[a][c] in [1,2] :
                    break
                mat[a][c]  = 3
            for c in range(b+1,n):
                if mat[a][c] in [1,2]:
                    break
                mat[a][c] = 3 


        for a,b in guards:
            mark_guarded(a,b)

        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] ==0:
                    res+=1
        print(mat)
        return res 