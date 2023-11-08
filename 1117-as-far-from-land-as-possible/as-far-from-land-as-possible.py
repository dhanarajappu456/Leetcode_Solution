from collections import deque as dq 


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m,n  = len(grid),len(grid[0])
        def out(x,y):

            if x<0 or y<0 or x>=m or y>=n: 
                return True
            return False

        q =dq([ ])
        vis  = set( )
        dir =[(0,1),(0,-1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    vis.add((i,j))
                    q.append((i,j,0))

        ans=0 
        while(q):

            i,j , dist = q.popleft()
            ans = max(ans, dist)
            for d in dir:
                x,y = i+d[0],j+d[1]
                if (not out(x,y)) and ((x,y) not in vis )and grid[x][y]==0:
                    vis.add((x,y))
                    q.append((x,y,dist+1))
        

        return -1 if ans ==0 else ans 


        





        