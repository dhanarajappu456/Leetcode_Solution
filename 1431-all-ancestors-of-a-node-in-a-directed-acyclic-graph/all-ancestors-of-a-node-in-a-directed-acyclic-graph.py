class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        adj =  defaultdict(list)
        ans =   defaultdict(set)
        indeg= [0 for i in range(n)]

        # t: e
        for a,b in edges:
            adj[a].append(b)
            indeg[b]+=1
        q=deque([ i for i in range(n) if indeg[i] ==0 ])
        while( q): # t: n+e

            node= q.popleft()

            for nb in adj[node]:  # t :n*e , combining all the n iteration,the n from inner set union
            

                ans[nb] = ans[nb].union(ans[node])
                ans[nb].add(node)
                indeg[nb]-=1
                if indeg[nb] == 0:
                    q.append(nb)
        # n^2logn worst upper bound , not that much really 
        # as all  node cant have n number of  ancestor nodes
        res =[ 0 for i in range(n)]
        for i in range(n):

            res[i] = sorted(list(ans[i]))

        return res

        


        