from collections import deque
import heapq as h
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

        max_heap  = [(-near[0][0],0,0)]
        vis  = set()
        vis.add((0,0))
        while(max_heap):
            mx,i,j = h.heappop(max_heap)
            if (i == n-1 )and (j==n-1):
                return -mx
            for dr in d:
                x,y = i+dr[0] , j+dr[1]
                if  (0<=x<n) and (0<=y<n) and  (( x,y  ) not in vis):
                    vis.add((x,y))
                    h.heappush(max_heap,(-min(-mx,near[x][y]),x,y))