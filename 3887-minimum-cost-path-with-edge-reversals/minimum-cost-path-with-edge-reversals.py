import heapq as h 

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        adj  = defaultdict(list)
        indegree = defaultdict(list)

        #create the indegree  node and their 2*wt
        for a,b,w in edges:
            adj[a].append((b,w))

            indegree[b].append((a,2*w))

        min_heap =[(0,0)]
        d = [ float("inf") for i in range(n)]
        d[0] = 0
        while(min_heap):

            node_wt, node = h.heappop(min_heap)
            if node  == n-1:
                return d[node]
            # push the nb  node to current node
            for nb,nb_wt in adj[node]:
                if node_wt + nb_wt < d[nb]:
                    h.heappush(min_heap,( node_wt + nb_wt,nb))
                    d[nb] = node_wt +nb_wt
            # push the nbs indegree to this current node
            for nb,nb_wt in indegree[node]:
                if node_wt + nb_wt < d[nb]:
                    h.heappush(min_heap,( node_wt + nb_wt, nb))
                    d[nb] = node_wt +nb_wt
            


        return -1
                