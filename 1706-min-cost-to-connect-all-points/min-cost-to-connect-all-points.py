class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #the idea is simple 
        #1)we choose a parentpoint and check which is the nearest unconnected ,point that we can connect to 
        # 2)the nearest point is got by checking the min distance update in the dist array, 
        #(where the dist[i] always keep track of the distance to the nearest point out of all the n points.)
        #3)then the chosen point is assumed to be connected and is flagged as connected
        #4) the chosen point now becomes the parent point , 

        #this is repeated till we get n-1 edged

        #we can also apply prims or kruskal algo in this, 
        #the given approarch mimic prim's algo in a fashion

        
        n = len(points)
        dist = [float("inf") for i in range(n)]
        connected = [False for i in range(n)]
        res = 0
        parentPoint  = 0
        for edges in range(n-1):
            
            connected[parentPoint] = True
            #choosing the parent point , then check which is the nearest point that it can connect to
            for point in range(n):
                
                if connected[point] == True:
                    continue
                dist[point] = min(dist[point], self.manhattan(points[point],points[parentPoint]))
            #nearest point among all the unconnected point is chosen
            dis , ind = min((dis,ind) for ind,dis in enumerate(dist) if connected[ind] == False)
            res+=dis
            parentPoint  = ind
      
        return res
                
        

    def manhattan(self, p1, p2) -> float:
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
        