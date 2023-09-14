from collections import defaultdict as dict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        #create the adjlist for a place , where each destiantion from the place is in the sorted order

        
        #traverse the graph in dfs way , wehre a node  might be visited multiple time 
        #but a edge should be visited only once, for a paticular source,  if we visit a neib , then we mark it -1  in the adj[src] so that , we don't visit it again from the same source, if the path dont lead to a solution , then we should change -1 back  to the neib value 



       

        tickets.sort()
        adj = dict(list)
        for src, dest in tickets:
            adj[src].append(dest)
   
        visited = set()
        path  =[]
        ans = []
        def dfs(src):
            nonlocal ans
            path.append(src)

            #each edge visited  adds a new node or place into the path , so total nodes in the path after visitng all edge(utilising all the ticket ) is  total edge + 1(that is including the source node "jfk")
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