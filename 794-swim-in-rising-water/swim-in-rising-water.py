import heapq as h 

class Solution:

    
    def swimInWater(self, grid: List[List[int]]) -> int:
        m,n  = len(grid) , len(grid[0])
        def valid(i,j):

            return 0<=i<m and 0<=j<n


        minHeap  = []
        ans  = [[float("inf") for j in range(n)] for i in range(m)]
        ans[0][0] = grid[0][0]
        h.heappush(  minHeap , (grid[0][0],0,0))
        d  = [(0,-1),(0,1),(1,0), (-1,0) ]
        while(minHeap):

            t,i,j = h.heappop(minHeap)
            if i ==m-1 and j==n-1:
                return t 
            for dx,dy in d:

                x,y = i+dx , j+dy
                if valid(x,y):
                    time = max(t,grid[x][y])
                    if time < ans[x][y]:

                        ans[x][y] =  time 
                        h.heappush(minHeap , (time,x,y))
           
