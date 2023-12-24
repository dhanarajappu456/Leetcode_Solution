'''
the solution is simple , that , we need to see that 

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
            why use the vis - to add the processed node with value val

            for the nodes with value val , there may be case they are adjacent to each other 
            in which case we need to avoid re-processing the node again , so we put it in  the vis set 
            like
            vals =[1,1]
            edges =[0,1]
            '''
            vis = set()
            par_val_count = initialize_par_val_count(val)

            for node in val_node[val]:
                
                for neib in adj[node]:
                    p1 = ds.findPar(node)
                    p2 = ds.findPar(neib)
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
                #add the node as processed in to the vis
                vis.add(node)

        return ans + n

