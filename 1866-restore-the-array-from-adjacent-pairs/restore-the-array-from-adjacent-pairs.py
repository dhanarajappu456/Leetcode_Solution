from collections import defaultdict as dict 

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        vis = {}
        adj = dict(list)

        n = len(adjacentPairs)+1
        for p in adjacentPairs:

            a,b = p[0],p[1]

            adj[a].append(b)
            adj[b].append(a)

        start = None
        for i in adj: 
            if len(adj[i])==1:
                start = i
                break 
        ans = []
        vis  = set()
        while(len(ans)!=n):
            ans.append(start)
            vis.add(start)

            for adjacent in adj[start]:
                if adjacent not in vis:
                    start = adjacent
 
        return ans 


        