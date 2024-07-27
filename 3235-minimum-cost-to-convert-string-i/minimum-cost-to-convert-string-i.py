import heapq as h 

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
  

        #create the adj list
        adj = defaultdict(defaultdict)
        for i,a in enumerate(original):
            b= changed[i]
            w =cost[i]
            if b in adj[a] and adj[a][b]<w:
                continue
            adj[a][b] = w 

        cache = defaultdict(defaultdict)
        def shortest(s,d):
                if s in cache:
                    return cache[s][d]
                dis = {chr(97+i) : float("inf") for i in range(26)}
                dis[s] =0 
                min_heap = [(0,s)]
                while(min_heap):
                    wt, node  = h.heappop(min_heap)
                    for nb in adj[node]:
                        w = adj[node][nb]
                        if dis[nb]> w+wt:
                            dis[nb] = w+wt
                            h.heappush(min_heap,(dis[nb], nb))
                for node in dis:
                    cache[s][node] = -1  if dis[node] == float("inf")  else dis[node]
                if dis[d]==float("inf"):
                    return -1
                return dis[d]



        #for each pair of transformation in the char check the min/shortest cost in the graph
        ans  = 0 
        n = len(source)
        for i in range(n):
            s, d  = source[i], target[i]
            cost  = shortest(s,d)
            if cost == -1:
                return -1 
            ans += cost

        return ans 


        






        