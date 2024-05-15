from collections import deque
class Solution:
    def maximumSafenessFactor(self,grid):


        #creating a grid with info where each cell value =  dist to nearest one
        #using bfs
        q =deque([])
        m,n = len(grid), len(grid[0])
        near = [[float("inf") for j in range(n)] for i in range(m) ]
        vis  = set()
        for  i in range(m) :
            for j in range(n):
                if grid[i][j] ==1:
                    near[i][j]=0
                    q.append((i,j,0))
                    vis.add((i,j))
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        while(q):
            i,j,dis = q.popleft()
            for dr in d: 
                x,y  = i+dr[0] ,j+dr[1]
                if (0<=x<m) and (0<=y<n) and  (( x,y  ) not in vis) : 
                    q.append((x,y,dis+1))
                    near[x][y] = dis+1
                    vis.add((x,y))   
    
        def possible(saf_fact):
            q= deque([])
            vis  = set()
            if near[0][0]>=saf_fact:
                q.append((0,0))
                vis.add((0,0)) 
            while(q):
                i,j  = q.popleft()
                if i==n-1 and j== n-1:
                    return True
                for dr in d:
                    x,y  = i+dr[0], j+dr[1]
                    if 0<=x<n and 0<=y<n and ((x,y) not in  vis)  and (near[x][y]>=saf_fact):
                        vis.add((x,y))
                        q.append((x,y))
            return False

        l,h =0,400
        ans  = -1 
        while(l<=h):
            m = (l+h)//2
            if possible(m):
                l=m+1
                ans  = m 
            else:
                h = m-1
        return ans 
                    
               
