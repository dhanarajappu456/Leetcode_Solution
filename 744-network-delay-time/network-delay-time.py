from collections import deque ,defaultdict as dict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist  =[float("inf") for i in range(n+1)]
        adj = dict(list)
        for s,d,t in times:

            adj[s].append((d,t))

        q=deque([(k,0)])
        dist[k] = 0 
        ans = 0
        while(q):


            node, node_t = q.popleft()

            for neib,neib_t in adj[node]:
                
                if node_t +  neib_t<dist[neib]:
                    q.append((neib,node_t+neib_t))
                    dist[neib] = neib_t + node_t
        ans = max(dist[1:])  
        return -1 if ans==float("inf")  else ans





            


        
        