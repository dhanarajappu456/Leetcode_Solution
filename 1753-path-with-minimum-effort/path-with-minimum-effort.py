import heapq as h 
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n  = len(heights), len(heights[0])
        efforts = [[ float("inf") for j in range(n)] for i in range(m)]
        efforts[0][0]  = 0
        priorQ = []
        h.heapify(priorQ)
        dir_ =[(-1,0),(0,1),(1,0),(0,-1)]
        h.heappush(priorQ,(0,0,0))
        def isValidCell(x,y):
            if x>-1 and x<m and y>-1 and y<n:
                return True
            return False
        while(True):#V
            effortNode , i,j = h.heappop(priorQ) #logv
            if (i,j) ==(m-1,n-1):
                return effortNode
            for d in dir_ :
                
                x = i + d[0]
                y = j + d[1]
                
                if isValidCell(x,y):
                    
                    #V at max allnode connected all other nodes
       
                    if max(effortNode , abs(heights[i][j] - heights[x][y]))< efforts[x][y]:
                        
                        efforts[x][y] = max(effortNode , abs(heights[i][j] - heights[x][y])) 
                        h.heappush(priorQ, (efforts[x][y],x,y) )#logv
               
         
    