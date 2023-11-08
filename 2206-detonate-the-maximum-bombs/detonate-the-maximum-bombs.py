from collections import defaultdict as dict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        adj = dict(list)

        n = len(bombs)
        for i in range(n):
            for j  in range(n):

                if i!=j:
                    x1,y1,r1 = bombs[i]
                    x2,y2,r2 = bombs[j]

                    if math.sqrt((x1-x2)**2 + (y1-y2)**2)<=r1:
                        adj[i].append(j)
        
        
 
        #cache the result
        memo = {}
        ans = 0
        def rec(node):
            if node in vis:
                return 0
            
            # not  count  redundant node that is visited as part of a starting node i 
            #eg: 0->1->2  0->2 , when we start dfs on 0 , it would visit 2 twice if we not use visited
            vis.add(node)
            #to note go back to cycle - in the same path  : or parent
            pathVis.add(node)
            nodes=0
            for neib in adj[node]:
                if neib not in pathVis:
                    nodes += rec(neib)
            pathVis.remove(node)
            memo[node] = 1 + nodes
            return memo[node]
        pathVis =set()
        vis  = set()
        ans  = 1 
        for i in range(n):
            
            vis = set()
            fn =  rec(i)
            ans =max(ans, fn)

        return ans

        