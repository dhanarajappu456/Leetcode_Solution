
from collections import defaultdict as dict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        #make undirected graph, start travelling from 0 , 
        #traverse from 0 in the unir graph
        #and see if the edge need be traversed


        adj = dict(list)

        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        connSet =set()
        for conn in connections:
            connSet.add(tuple(conn))
       
        visited = set()
        def rec(node): 

            if node in visited :
                return 0
            visited.add(node)
            ans =0
            for neib in adj[node]:
                if neib not in visited:

                    if (node, neib) in connSet:
                        ans+=1
                    ans+=rec(neib)
            return ans
        return rec(0)
                