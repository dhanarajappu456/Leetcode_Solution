
#djikstras algo

from collections import defaultdict as dict
import heapq as h 

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):

        self.adj   = dict(list)
        self.n = n 
        for edge in edges:
            s,d,w = edge
            self.adj[s].append((d,w))

  

    def addEdge(self, edge: List[int]) -> None:
        s,d,w = edge
        self.adj[s].append((d,w))

        

    def shortestPath(self, node1: int, node2: int) -> int:
        pq =  [(node1,0)]
        h.heapify(pq)
        self.dist = [ float("inf")  for i in range( self.n )]
        self.dist[node1] = 0 
        while(pq):
            node, nodeWt = h.heappop(pq)
            for neib,neibWt in self.adj[node]:
                if nodeWt +neibWt  <self.dist[neib]:
                    self.dist[neib]  = nodeWt +neibWt
                    h.heappush(pq,(neib,nodeWt +neibWt))
       
        return -1 if self.dist[node2]==float("inf") else self.dist[node2]


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)