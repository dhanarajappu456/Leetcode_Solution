class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        if len(edges)== 0:
            return [0]
        neib  = defaultdict(list)
        indegree = [0 for i in range(n)]
        for a,b in edges:
            neib[a].append(b)
            neib[b].append(a)
            indegree[a]+=1
            indegree[b]+=1

       
        q = deque([ i for i in range(n) if indegree[i] == 1 ])
        
        visited = set()
        while(n>2):
            
            size = len(q)
            n-=size
            indeg_nodes =set()
            for i in range(size):
                node = q.popleft()
                for nb in neib[node]:
                    indegree[nb]-=1
                    if indegree[nb]==1 :
                      
                        q.append(nb)
        
        return q
            
                    
                

        