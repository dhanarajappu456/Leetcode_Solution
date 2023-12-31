from collections import defaultdict as dict 

#fails when pseudo - criti = pseduo

# [[0,1,1],[0,3,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1]]

# Output
# [[],[0,1,2,3,4]]
# Expected
# [[],[0,1,2,3,4,5]]

class DSU:
    def __init__(self,V):
        self.rank  = [1 for i in range(V)]
        self.parent = [i  for i in range(V)]
    #o(4*alpha) =O(1)
    def union(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        if self.rank[pu] <self.rank[pv]:
            self.parent[pu] =pv 
          
        elif self.rank[pu] >self.rank[pv]:
            
            self.parent[pv] =pu
           
        else:
            self.parent[pv]=pu
            self.rank[pu]+= 1 
            
    
    def findParent(self,u):
        
        if self.parent[u]==u:
            return u
       
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
       
        def kruskal(edges,skip_edge,add_edge):
           
            ds = DSU(n)
            mst_sum  = 0 
            edges_used =0 
            if add_edge!=-1:
                a,b,w,ind = edges[add_edge]
                pa,pb = ds.findParent(a),ds.findParent(b)
                ds.union(pa,pb)
                edges_used+=1
                mst_sum+= w

            for i in range(len(edges)):
                if i== skip_edge:
                    continue
                

                edge =edges[i]
                
                a,b,w,ind  = edge
                pa,pb = ds.findParent(a), ds.findParent(b)
                if pa!=pb:
                    ds.union(a,b) 
                    edges_used+=1
                    mst_sum+= w
    
            return (mst_sum,edges_used)

        edge_list= []
        for i in range(len(edges)):
            a,b,w = edges[i]
            edge_list.append([a,b,w,i])
        edges = edge_list
        edges.sort(key = lambda x:x[2])

        actual_mst_sum,edges_used= kruskal(edges,-1,-1)
        
        crit= []
        pseudo = []
        for i in range(len(edges)):
            a,b,w,ind = edges[i]
            mst_sum , edges_used = kruskal(edges,i,-1)
         
            if mst_sum > actual_mst_sum  or edges_used != n-1:
                crit.append(ind)
            

            else:
                mst_sum , edges_used = kruskal(edges,-1,i)
                if(mst_sum == actual_mst_sum  and edges_used == n-1):
                   
                    pseudo.append(ind)
            
            

        return [crit,pseudo]



        