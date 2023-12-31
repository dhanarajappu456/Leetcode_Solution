'''

solution is simple , we need to find traverse that component which has the node 1 , as the graph my be disconnected, 
then find min edge weight in that component

t  e
s  e

way1   - visited set store the edges
_______________
remember we need to traverse all the edge in the component so visited set must be storing the bidirectional edge  as visited 

way2 - vis store vertex 
you can also store just vertex, 

traverse the edge which leads to vertex already visited  and call the dfs for the already called vertex, then return back the recursion in the base case
'''

from collections import defaultdict as dict

# #way1 
# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:

#         adj =dict(list)


#         for a,b, w in roads:
#             adj[a].append((b,w))
#             adj[b].append((a,w))

#         ans =[float("inf")]
#         vis = set()
#         def dfs(node):


#             for neib,w  in adj[node]:
#                 if (node , neib ,w ) not in vis:  
#                     vis.add((node,neib ,w ))
#                     vis.add((neib,node ,w ))
#                     ans[0] = min(ans[0],w)
#                     dfs(neib)
#         dfs(1)
#         return ans[0]
# #way 2
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int: 
        adj = defaultdict(list) # node -> list of (neighbor, dist) for src, dst, dist in roads:
        for src, dst,dist  in roads: 
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for nei, dist in adj[i]: 
                res = min(res, dist) 
                dfs(nei)
        res = float("inf")
        visit = set()
        dfs(1)
        return res



        