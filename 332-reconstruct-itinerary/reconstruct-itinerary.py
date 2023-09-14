from collections import defaultdict as dict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        #create the adjlist for a place , where each destiantion from the place is in the sorted order

        
        #traverse the graph in dfs way , wehre a node  might be visited multiple time 
        #but a edge should be visited only once,   which should be kept track of in a visited edge 

       

        tickets.sort()
        adj = dict(list)
        for src, dest in tickets:
            adj[src].append(dest)
   
        print(adj)
        visited = set()
        path  =[]
        ans = []
        def dfs(src):
            nonlocal ans
            path.append(src)
            #print(src,path)
            if len(path) == len(tickets)+1:
                
                ans=path.copy()
                return True
    
            for i in range(len(adj[src])):
               
                if  adj[src][i]!= -1:
                    neib = adj[src][i]
                    adj[src][i] = -1
                    if dfs(neib) :
                        
                        return True
                    adj[src][i] = neib
                    
        
            path.pop(-1)

            return False

        dfs("JFK")
        return ans