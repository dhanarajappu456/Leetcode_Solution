from collections import defaultdict as dict 
'''
we use kruskal algo to find the mst here 


first calculate the mst sum value for the given graph
1)checking critical edges is simple 
simply try skipping that edge and see if can yield a spanning tree whose sum is that of mst
2) checking if edge is pseudo critical 

if the edge is not critical it migh be pseudo , but not for sure , 

for edge to be pseudo edge it must be an edge that is part of some spanning tree
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]

in this graph edge 6 is neither critcal nor pseudo critical 

so we should take care of this edge case


to check if a edge which is not critical as pseduo critical , just force add the edge to a the tree and try forming spanning tree and check if we can get a mst tree with this, if we get mst , then this edge we force added is part of some mst and therefore is pseudo , else not pseudo 
t eloge + e^2
s : V(parent and rank) + e(reformed edgelist)
'''

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
            # time :e 
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

        #reform edges, to preserve original index, 
        #while sorting
        #new edge look of form [a,b, w , old_ind]
        edge_list= []
        # time :e 
        for i in range(len(edges)):
            a,b,w = edges[i]
            edge_list.append([a,b,w,i])
        edges = edge_list
        edges.sort(key = lambda x:x[2])
        actual_mst_sum,edges_used= kruskal(edges,-1,-1)
        
        crit , pseudo = [],[]
        # time :e 
        for i in range(len(edges)):
            a,b,w,ind = edges[i]
            mst_sum , edges_used = kruskal(edges,i,-1)

            #checking critical edge
            #when edge is critical , we cant get a spanning tree of sum == actual mst tree's sum , or we can still get some == mst tree's sum 
            # but would not be a tree connecting all vertex(ie will be disjoint)
            if mst_sum > actual_mst_sum  or edges_used != n-1:
                crit.append(ind)
            #checking pseudo critical edge
            
            else:
                #if we can get a spanning tree whose sum is == actual mst 
                #then edge is pseudo
                mst_sum , edges_used = kruskal(edges,-1,i)
                if(mst_sum == actual_mst_sum  and edges_used == n-1):
                    pseudo.append(ind)
            
            

        return [crit,pseudo]



        