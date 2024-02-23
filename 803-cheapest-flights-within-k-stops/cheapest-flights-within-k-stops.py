

'''
#solution1  -- simple bfs 
t more than v+e ( since same node will be visited more than once) approx , e^2 ( since constraint small) 
pass the test case 
s v+e 

#solution 2 

t ve
s v+e 

'''

# #solution1  -- simple bfs 
from collections import defaultdict as dict 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = float("inf")

        q  = deque([(src,0)])
        boundary =0
        adj =dict(list)

        for s,d,w in flights:
            adj[s].append((d ,w ))
        dist =[float("inf") for i in range(n)]
        dist[src] = 0 
        
        while(q and ( boundary<=k)):
            l =len(q)
            for l in range(l):

                node, node_dist = q.popleft()

                
                for neib , neib_dist1 in adj[node]:
                    neib_dist2 = node_dist  + neib_dist1
                    if neib_dist2 < dist[neib]:
                        dist[neib] = min(dis[neib], neib_dist2)
                        q.append((neib, dist[neib]))
               
            boundary+=1 
        return  - 1 if dist[dst] ==float("inf") else  dist[dst] 
     


#solution2  -- bellman ford
'''

Note the use of temp array here,  In  each iteration(which ideally is moving 1 step in the frontier)
 we might  end up updating dist array for many nodes  in  frontiers which are more than 1 step ahead  ,
  in an iteration, this happens , if the order of edge given is same as teh order of
   the edges in the graph (from the source) 

eg \U0001f44d

n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1


To avoid this we use temp which stores the min dist of all nodes till previous frontier traversal, 
Based on which we calculate the dist of all nodes in the current frontier traversal 
, which is updated in dist array.This is copied to temp at the end of frontier traversal 


t ve
s v(for the dist array)
'''
from collections import defaultdict as dict 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = float("inf")

   
    
        dist =[float("inf") for i in range(n)]
        dist[src] = 0 
        temp = dist.copy()    
        for i in range(k+1):

            for node, neib, neib_cost in flights: 

                dist[neib] =  min(dist[neib], temp[node]+neib_cost)
            
            temp= dist.copy()
            
    
        return  - 1 if dist[dst] ==float("inf") else  dist[dst] 
     


        