class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for i in range(0,n-1): 
            adj[i].append(i+1)

        def bfs(node):
            q = deque([node])
            vis  = set( )
            vis.add(0)
            d = 0
            while(q):
                l = len(q)
                for i in range(l):
                    node  = q.popleft()
                    for neib in adj[node]:
                        if neib  == n-1:
                            return d+1 
                        if neib not in vis:
                            vis.add(neib)
                            q.append(neib)
                d+=1 
            return -1 

        res = []
        for i in range(len(queries)):
            a,b  = queries[i][0] ,queries[i][1]
            adj[a].append(b)
            ans = bfs(0)
            res.append(ans)
        return res 

                
                


