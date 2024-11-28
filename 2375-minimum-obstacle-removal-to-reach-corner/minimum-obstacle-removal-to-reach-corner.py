import heapq as h 

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        d = [[ float("inf") for j in range(n)] for i in range(m)]
        min_heap = [(grid[0][0], 0,0)]
        d[0][0] = grid[0][0]
        h.heapify(min_heap)
        dir_ = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while(min_heap):
            dist_,x,y= h.heappop(min_heap)
            if (x== m-1) and (y == n-1):
                return dist_
            for i,j in dir_:
                a,b = x+i , y+j
                if (0<=a<m) and (0<=b<n) and ((dist_ + grid[a][b] )< d[a][b]):
                    d[a][b] = dist_ + grid[a][b] 
                    h.heappush(min_heap,(dist_+grid[a][b],a,b))

        return -1




