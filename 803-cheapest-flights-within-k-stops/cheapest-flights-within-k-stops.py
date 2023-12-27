

'''
#solution1  -- simple bfs 
t more than v+e ( since same node will be visited more than once) approx , e^2 ( since constraint small) 
pass the test case 
s v+e 
'''

#solution1  -- simple bfs 
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
                        dist[neib] = neib_dist2
                        q.append((neib, dist[neib]))
               
            boundary+=1 
        return  - 1 if dist[dst] ==float("inf") else  dist[dst] 
     


        