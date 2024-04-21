from collections import defaultdict as dict 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        s,d = source, destination 

        adj = dict(list)
        vis  =set()
        for e in edges: 

            adj[e[0]].append(e[1])
            adj[e[1]].append (e[0])
        def rec(s):
           
            if s == d: 
                return True
            vis.add(s)
          
            for neib in adj[s]:
                if (neib not in vis) and rec(neib):
                    return True
            return False
            
        return rec(s)

        