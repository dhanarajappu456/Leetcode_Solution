from collections import defaultdict as dict
import time
from collections import defaultdict as dict 


class Solution:
    def findItinerary(self, tickets):
        

        #create adj list , with neibs sorted
        tickets.sort()

        adj  = dict(list)

        for a,b in  tickets:
            adj[a].append(b)
        
        ans  =[]
        def rec(node,edge_traversed):
            # print(node, edge_traversed)
            # print(adj)
            # if node =="SFO":
            #     time.sleep(134345550)
            
    
            # if edge_traversed == len(tickets): 
                
            #     return True
            
            for  i in range(len(adj[node])):
                neib  = adj[node][i]
                if neib != -1:

                    
                    adj[node][i]=-1
                    
                    rec(neib,edge_traversed+1 )
                    

                    

            ans.append(node)
           
           

        rec("JFK",0)
        return ans[::-1]
