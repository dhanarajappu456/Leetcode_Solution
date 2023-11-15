# solution 1 dfs/bfs traversal   - wrong answer 

# traverse the graph and identify any  edge in cycle - but this gives wrong ans 

# since the questions says, if there are multiple ans , we need to return las occuring edge in the edge list
# which is hard to find in this treversal way

# so better solution is apply union find which process each edge in the same order as given in the list 

# t  v+ e 
# s v+ e

# solution 2 - union find - union by rank and path compression 

# t  calls(number of calls to union == number of edges addded )
# s  n(parent , rank array)




#solution 1 dfs traversal


# from collections import defaultdict as dict
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         adj = dict(list)
#         ans = [None]


#         for a,b in edges:

#             adj[a].append(b)
#             adj[b].append(a)

#         vis = set()

#         def rec(node,parent):

#             if node in vis:
#                 ans[0] = [parent,node]
        
#                 return 
            
#             vis.add(node)

#             for neib in adj[node]:

#                 if neib==parent:
#                     continue

#                 rec(node,neib)

        
#         rec(1,0)
#         return ans[0]


#solution 2 - union find 


class Disjoint:

    def __init__(self,n):

        self.rank = [ 0 for i in range(n+1)]
        self.parent= [i for i in range(n+1)]

    def union(self,u,v):

        pu,pv  = self.findPar(u),self.findPar(v)
        if self.rank[pu]< self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu]> self.rank[pv]:
            self.parent[pv]= self.parent[pu]
        else: 
            self.parent[pu] = self.parent[pv]
            self.rank[pv]+=1

    def findPar(self,u):

        if self.parent[u] == u:
            return u 

        par  = self.findPar(self.parent[u])
        self.parent[u] = par
        return par
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n  = len(edges)
        ds = Disjoint(n)


        for a,b  in edges:
            pu,pv = ds.findPar(a), ds.findPar(b)

            if pu==pv:
                return [a,b]

            ds.union(pu,pv)
        

