import heapq as h 
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        

        
        if (grid[0][1] >1) and (grid[1][0] > 1) : 
            return -1
        m,n = len(grid),len(grid[0])
        d = [[ float("inf") for j in range(n)] for i in range(m)]
        min_heap = [(grid[0][0], 0,0)]
        d[0][0] = grid[0][0]
        h.heapify(min_heap)
        dir_ = [(0,1),(0,-1),(1,0),(-1,0)]
        dist_mat =[[float("inf") for j in range(n)] for i in range(m)]
        dist_mat[0][0] = 0
        while(min_heap):
            dist_,x,y= h.heappop(min_heap)
            
            if (x== m-1) and (y == n-1):
                return dist_
            for i,j in dir_:
                a,b = x+i , y+j
                if (0<=a<m) and (0<=b<n):
                    # calculated time to reach neibr 
                    # 1. when diff is odd and diff is even
                    new_dist = 0 
                    distance = grid[a][b] - dist_
                    if  distance<=0:
                        new_dist  = dist_+1
                    else:
                        if  distance %2 ==0:
                            new_dist = grid[a][b]+1
                        else:
                            new_dist = grid[a][b]
                    
                    if new_dist < dist_mat[a][b]:
                        dist_mat[a][b] = dist_
                        h.heappush(min_heap,(new_dist ,a,b))
       
        return -1

