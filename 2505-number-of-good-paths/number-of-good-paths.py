'''

#solution 1 - dfs or bfs 

for each node as the starting node we explore all path that end with same value as that of the node

t n*n
s  n(stk space in case of dfs or q space in case of bfs) + adjlist(v+e) , 


#solution 2 - using disjoint set

when we check all the good path where start and end values is val and all nodes in the graph has value  <=val 
then it is easy to calculte the number of good path with val as start and end .

suppose we have n1 nodes with value val 
then this ans  = n1C2 , that is each pair of node with value n1 as the start and end.

We build the graph such that we add nodes to the graph based on the increasing order of the value(val) it has  .Thus ensuring all the nodes in the graph has value<=val at any instant , thus makees computation and problem  easy 

thus graph will be disjoint component as we add the new nodes or (edges) , so we come to use  DSU.

in each component the ultimate parent of the component keeps count of nodes in it with current value val(in a map par_val_count)


t  nlogn + n  
s  adj + rank+ par = n+e + n + n 


'''
from collections import defaultdict

class DSU:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def findPar(self, u):
        if self.par[u] == u:
            return u
        self.par[u] = self.findPar(self.par[u])
        return self.par[u]

    def union(self, u, v):
        pu, pv = self.findPar(u), self.findPar(v)
        ultimate_par = None
        if self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
            ultimate_par = pv
        elif self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
            ultimate_par = pu
        else:
            self.par[pu] = pv
            self.rank[pv] += 1
            ultimate_par = pv
        return ultimate_par


class Solution:
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)
        ds = DSU(n)
        val_node = defaultdict(list)

        # create val_to_node map
        for i in range(n):
            val = vals[i]
            val_node[val].append(i)

        # create adj list
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        ans = 0

        def initialize_par_val_count(val):
            d = defaultdict(int)
            for node in val_node[val]:
                d[node] = 1
            return d

        for val in sorted(val_node.keys()):
            '''
           

           
            '''
            #this keeps parent of each component mapped to number of nodes in it , with current value val
            #this count is used in teh computation when we add new node / edge 
            par_val_count = initialize_par_val_count(val)

            for node in val_node[val]:
                
                for neib in adj[node]:
                    p1 = ds.findPar(node)
                    p2 = ds.findPar(neib)
                    '''
                    for the nodes with value val , there may be case they are adjacent to each other 
                    in which case we need to avoid re-processing the node again as it is already computed and 
                    belongs to same component  so we check p1 != p2  you can either make use of a vis set instead of checking this , to put all nodes with value val that is already processed
                    eg
                    vals =[1,1]
                    edges =[0,1]

                    
                    '''
                    if vals[neib] <= val and p1!=p2:
               
                        
                        #number of nodes in the comp1
                        count1 = par_val_count[p1]
                        #number of nodes in the comp2 
                        count2 = par_val_count[p2]
                        '''
                        when the node need to be joined to neib , 
                        let node be in comp1 , and neib in comp2 
                        we get good path such
                        1) that  current node (node) as starting forms the 
                        path with nodes(with val) in comp2
                        2) all nodes(with val)in comp1 forms good path with all nodes(with val )
                        in the comp2 
                        '''
                        ans += (count2 + (max(0, count1 - 1) * count2))
                        ult_par = ds.union(p1, p2)
                        #the number of nodes with value val in the combined component now becomes 
                        #count1+count2
                        #which is stored in the map , where ultimate parent of the combined component 
                        #represent this value, and is used as the key
                        par_val_count[ult_par] = count2 + count1
          
        #each individual node is a good path by itself. 
        return ans + n

