from collections import  deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        m,n  = len(grid), len(grid[0])
        def out_bound(i,j):
            # print("out ",i,j)
            if i<0 or j<0 or i>=m or j>=n:
                return True
            return False

    
       

        if (grid[0][0] == 1) or (grid[m-1][n-1] == 1):
            return -1
        vis = set()
        q = deque([(0,0,1)])
        d = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

        while(q):
            x,y,step = q.popleft()
            if x == m-1 and y == n-1:
                return  step
            for dr in d:
                i,j  = x+dr[0] , y+dr[1]
                if  (not out_bound(i,j)) and  ((i,j) not in vis)  and  (grid[i][j] == 0):
                    vis.add((i,j))
                    q.append((i,j,step+1))
        


        return -1
        
        
                
                

                

                







