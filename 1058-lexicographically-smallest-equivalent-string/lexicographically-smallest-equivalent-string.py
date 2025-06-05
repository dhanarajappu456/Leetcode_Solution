from collections import defaultdict as dict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = dict(list)
        n = len(s1)
        for i in range(n):
            a = s1[i]
            b = s2[i]
            adj[a].append(b)
            adj[b].append(a)
        vis  = set()
        min_ = "z"
        #print(adj)
        def dfs(c):
            nonlocal min_
            #print(c )
            min_   = min(min_, c)
            vis.add(c)
            for nb in adj[c]:
                if nb not in vis:
                    dfs(nb)
            
        
        s =  ""
        for c in baseStr:
            vis  = set()
            min_ = "z"
            dfs(c)
            s+=min_
        
        return s