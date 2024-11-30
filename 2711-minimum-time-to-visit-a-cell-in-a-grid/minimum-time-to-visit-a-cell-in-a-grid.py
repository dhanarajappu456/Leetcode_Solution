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
        time_mat =[[float("inf") for j in range(n)] for i in range(m)]
        time_mat[0][0] = 0
        while(min_heap):
            time_,x,y= h.heappop(min_heap)
          
            if (x== m-1) and (y == n-1):
                return time_
            for i,j in dir_:
                a,b = x+i , y+j
                if (0<=a<m) and (0<=b<n):
                   
                    next_time = 0 
                    time_diff = grid[a][b] - time_
                    if  time_diff<=0:
                        #if neibr has a value <=time_taken so far
                        #then time time to reach it is time_+1 
                        #where time_ is , time taken so far 
                        next_time  = time_+1
                    else:
                        # calculate time to reach neibr 
                        # 1. when time diff is odd and diff is even
                  
                        if  time_diff %2 ==0:
                        
                            next_time = grid[a][b]+1
                        else:
                            next_time = grid[a][b]
                    
                    if next_time < time_mat[a][b]:
                        time_mat[a][b] = time_
                        h.heappush(min_heap,(next_time ,a,b))
       
        return -1

