class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        
        m,n  =len(grid1),len(grid1[0])
        vis  = set()
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def outBound(i,j):
            return i<0 or i>=m or j<0 or j>=n
        def rec(i,j):


            if outBound(i,j) or ((i,j)  in vis) or grid2[i][j]==0:
         
                return True
            curr = True
            if grid1[i][j]!=grid2[i][j]:
            
                curr=False
                
    
            vis.add((i,j))
         
            for d in dir:
                x = i+  d[0] 
                y = j + d[1]
                #this line very important , dont write  curr and rec(x,y)
                # bcz, due to short ciruit, when curr is False(that is curr cll in grid 1 is not 1 )
                # the  the rec will not be called , so place curr after rec
                curr = rec(x,y) and curr
            return curr
        
        ans =0 
        for i in range(m):
            for j in range(n):
                if ((i,j) not in vis )and grid2[i][j]==1 :
                    if rec(i,j):
                        ans+=1
        return ans 



        