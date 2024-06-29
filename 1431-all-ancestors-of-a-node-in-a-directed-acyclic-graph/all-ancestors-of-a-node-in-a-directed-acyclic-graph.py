class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        adj =  defaultdict(list)

        ans =   defaultdict(set)
        indeg= [0 for i in range(n)]


        for a,b in edges:
            adj[a].append(b)
            indeg[b]+=1
        q=deque([ i for i in range(n) if indeg[i] ==0 ])
        while( q):

            node= q.popleft()

            for nb in adj[node]:
                ans[nb] = ans[nb].union(ans[node])
                ans[nb].add(node)
                indeg[nb]-=1
                if indeg[nb] == 0:
                    q.append(nb)
        res =[ 0 for i in range(n)]
        for i in range(n):

            res[i] = sorted(list(ans[i]))

        return res

        


        