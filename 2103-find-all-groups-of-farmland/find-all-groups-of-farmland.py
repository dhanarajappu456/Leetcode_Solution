'''
can use the dfs or bfs 
as it is said that when no two different farm lands are 4 driectioanlly adjavcemt 

means say when current row r1 has 5 1's continuosly say from c1 to c1 , then , 
then next row r2 should have 5 1's aligning to this , if at all 
there is a 1 in any column from c1 to c2. 

using this fact we can implement anothre solution apart from bfs 

which is given below
t n^2(overall n^2) 
s  1

'''
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n  = len(land) , len(land[0])
        res= []
        #helper finding the top-left and bottom right corner
        def helper(i,j):
            #top left is r1 ,c2
            r1,c1 = i,j
            #bottom right is found using algo below
            r2,c2 = i,j
            #moving the c2 till we see a 1 
            while((c2<n) and( land[r2][c2]==1)):
                #marking this 1 as -1 so as to not visit again
                land[r2][c2]= -1
                c2+=1
            c2-=1
            #if at all next rows has 1 b/w c1 and c2, then it must be continuosly from c1 to c2 
            r2+=1
            while((r2<m ) and (land[r2][c2]==1)):
                for col in range(c1,c2+1):
                     #marking this 1 as -1 so as to not visit again
                    land[r2][col]= -1
                r2+=1
            r2-=1
            return [r1,c1,r2,c2]
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    res.append(helper(i,j))

        return res