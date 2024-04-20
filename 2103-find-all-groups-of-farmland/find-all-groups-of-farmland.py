class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n  = len(land) , len(land[0])
        res= []
        def helper(i,j):
            r1,c1 = i,j
            r2,c2 = i,j
            while((c2<n) and( land[r2][c2]==1)):
               
                land[r2][c2]= -1
                c2+=1
            c2-=1
            
            r2+=1
            while((r2<m ) and (land[r2][c2]==1)):
                for col in range(c1,c2+1):

                    land[r2][col]= -1
                r2+=1
            r2-=1
          
            return [r1,c1,r2,c2]
        for i in range(m):
            for j in range(n):

                if land[i][j] == 1:
                    res.append(helper(i,j))

        return res