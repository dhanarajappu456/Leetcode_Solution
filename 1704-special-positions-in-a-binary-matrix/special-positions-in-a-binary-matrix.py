'''
solution 1 

Naive solution 
for each 1 cell check if it is safe by iterating on its row and col

t mn*(m+n)= 10^6
s 1 

#solution 2 - using map 

create 2 map , on for row and other for col 
where we map 

row ind -> list of cols(where 1 present)
and col_ind -> list of rows(where 1 present)

t mn 
s mn 

'''
#solution 1
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


        