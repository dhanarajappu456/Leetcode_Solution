class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:


        firstVisitTime =[-1 for i in range(n)]
        lowestVisitTime =[float("inf") for i in range(n)]
        
        vis =set()
        ans =[]


        adj = { i:[] for i in range(n)}

        for  a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
     
        def dfs(node,parent , time):
      
            firstVisitTime[node] = time
            lowestVisitTime[node] = time

        

            vis.add(node)


            for neib in adj[node]:

                if neib not in vis:

                    dfs(neib,node, time+1)
                    
                    lowestVisitTime[node] = min( lowestVisitTime[node], lowestVisitTime[neib])
                    
                    if  lowestVisitTime[neib]> firstVisitTime[node]:
                        ans.append([node, neib])


                
                else:
                    #avoiding parent parent mistakenly considered part of cycle
                    if neib!=parent:

                        lowestVisitTime[node] = min( lowestVisitTime[node], firstVisitTime[neib])
       
        dfs(0,-1,1)
        print(firstVisitTime , lowestVisitTime)
        return ans 

                    




        