class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:


       
        length = 0
        n  = len(graph)
        q = deque([])
        visited  = set()
        for node in range(n): 
            visited.add((node , (1<<node)))
            q.append((node , (1<<node)))
      
        while(q):

            #push all the adjacent nodes  to the queue , which is not a visited state(node, mask)
            # the state indicate that reaching the node we have mask representing all the nodes traversed in the journey
            # getting the same (node , path means it is redundant journey )

         
            for   i in range( len(q)) :
                 
                 node, mask = q.popleft()
                 #if all the nodes have been visited, then the mask is 1111....1 for all the  n node position 
                 if mask == (1<<n)-1:
                     return  length
                # explore  the  the univisied neib
                 for neib in graph[node]:

                    if (neib , mask|(1<<neib))  in visited :
                         continue
                    else:
                        q.append((neib,mask|(1<<neib)))
                        visited.add((neib , mask|(1<<neib) ))
            length+=1

            '''we will visite a  node multiple times, with 2^n possibile bitmask 
            so time complexity is n*2^n

            space = n*2^n
            '''



            
        