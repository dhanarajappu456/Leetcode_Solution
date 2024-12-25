class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        #best strategy is to choose n1 and n2 and connect 
        #where n1 is mid node  of longest path b/w two nodes(diameter)
        #of the first tree
        #where n2 is the same thing for the second tree
    
        #so 
        #idea is to find the max path b/w 2 nodes in 
        #eaxh treee ( that is diameter)
        #then connect the nodes at the mid of this path 
        #in each tree
        self.max_d =0
        def two_max_find(curr, m1,m2):
            if curr>=m1: 
                
                m2=m1
                m1 = curr 
            elif curr>=m2:
                m2 = curr 
            return (m1,m2) 
        def dfs(nd,adj,vis):
            
            vis.add(nd)
            m1,m2 = 0,0
            for nb in adj[nd]:
                if nb not in vis:
                    d = dfs(nb,adj,vis)
                    m1,m2 = two_max_find(d,m1,m2)
           
            self.max_d  =max(self.max_d ,m1+m2)
            return max(m1,m2) + 1 
            
        
        adj1,adj2 = defaultdict(list), defaultdict(list)
        
      
       
        for a,b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)
           
        
        for a,b in edges2:
            adj2[a].append(b)
            adj2[b].append(a)
            
        
        dfs(0,adj1,set())
        dmx1 = self.max_d
 
        self.max_d = 0
        dfs(0,adj2,set())
        dmx2 = self.max_d

        return max(dmx1, dmx2,  math.ceil(dmx1/2) + math.ceil(dmx2/2)+1)
    

        