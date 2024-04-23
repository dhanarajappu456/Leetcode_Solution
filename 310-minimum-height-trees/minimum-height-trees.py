'''
The observation is leaf node(indegree 1 ) cant be  the answers and 
 also there are only at max  on or two nodes that gives the MHT 

 what we do is delete each leaf node at current istance , until we have <=2 remainig nodes

we use q here to process leaf nodes at each instatant at each instance
infact doing like khans algo

 t n
 s n

'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        if len(edges)== 0:
            return [0]
        neib  = defaultdict(list)
        #to identtify leaf node(indegree =1 )we use the indegree list
        indegree = [0 for i in range(n)]
        for a,b in edges:
            neib[a].append(b)
            neib[b].append(a)
            indegree[a]+=1
            indegree[b]+=1

       
        q = deque([ i for i in range(n) if indegree[i] == 1 ])
        #perform removal of leaf node until the number of nodes>2
        while(n>2):
            
            size = len(q)
            #we delete each leaf node at present from total nodes 
            n-=size
            for i in range(size):
                node = q.popleft()
                for nb in neib[node]:
                    indegree[nb]-=1
                    if indegree[nb]==1 :
                        q.append(nb)
        
        return q
            
                    
                

        