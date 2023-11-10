'''

solution is simple , we need to find traverse that component which has the node 1 , as the graph my be disconnected, 
then find min edge weight in that component

t  e
s  e

remember we need to traverse all the edge in the component so visited set must be storing the bidirectional edge  as visited , not the vertices
'''


from collections import defaultdict as dict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj =dict(list)


        for a,b, w in roads:
            adj[a].append((b,w))
            adj[b].append((a,w))

        ans =[float("inf")]
        vis = set()
        def dfs(node):


            for neib,w  in adj[node]:
                if (node , neib ,w ) not in vis:  
                    vis.add((node,neib ,w ))
                    vis.add((neib,node ,w ))
                    ans[0] = min(ans[0],w)
                    dfs(neib)
        dfs(1)
        return ans[0]
        



        