import heapq as h 
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        min_heap  =[] 
        h.heapify(min_heap)
        dirs  = [ (0,-1),(0,1),(1,0),(-1,0) ]
        time  = [[float("inf") for j in range(n)] for i in range(m)]
        time[0][0] = 0 
        min_heap =[(0, 2 , 0,0)]
        while(min_heap):
            t, prev,  x , y = h.heappop(min_heap)
            if (x == m-1) and( y == n-1):
                return t
            for  d in dirs:
                i,j  = x+d[0] , y+d[1]
                if 0<=i<m and 0<=j<n:
                    if prev == 1 :
                        curr = 2 
                        dist_  = max(t, moveTime[i][j]) + 2
                    else :
                        curr = 1 
                        dist_  = max(t, moveTime[i][j]) + 1 
                    if time[i][j] > dist_:
                        h.heappush(min_heap,(dist_ ,  curr , i, j))
                        time[i][j] = dist_
        return -1






# import heapq as h 
# class Solution:
#     def minTimeToReach(self, moveTime: List[List[int]]) -> int:
#         m, n = len(moveTime), len(moveTime[0])
#         min_heap  =[] 
#         h.heapify(min_heap)
#         dirs  = [ (0,-1),(0,1),(1,0),(-1,0) ]
#         time  = [[float("inf") for j in range(n)] for i in range(m)]
#         time[0][0] = 0 
#         min_heap =[(0,0,0)]
#         while(min_heap):
#             t, x , y = h.heappop(min_heap)
#             if (x == m-1) and( y == n-1):
#                 return t
#             for  d in dirs:
#                 i,j  = x+d[0] , y+d[1]
#                 if 0<=i<m and 0<=j<n:
#                     dist_  = max(t, moveTime[i][j])+1
#                     if time[i][j] > dist_:
#                         h.heappush(min_heap,(dist_ , i, j))
#                         time[i][j] = dist_
#         return -1
                


        
        