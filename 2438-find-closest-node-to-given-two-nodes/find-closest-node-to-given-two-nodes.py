'''

note that this is a simple graph, with just one outedge from any node. there fore u can have only 1 path from any node
also note that there are cycle


the solution asks for finding all the nodes that are common in the path from node1  , node 2 respectively

then for each common node  i we need to find that node which has the minimum max(dist_of_i_from_node1, dist_of_i_from_node2)
so we do a dfs (can do bfs also ) to  create map that maps nodes in path and their dist from the node1 or node2 

if there are multiple nodes i as the ans, that is same minimised maxdist from node1 and node2 , we need to return smaller value of i 
this multiple ans can occur when node1 and node2 is part of same cycle, where they cut the cycle in exct half 

t (v+e )= (n+ n ) (since there are no multiple edges from a single node, therefore we have single path starting from any node, thus max number of edges = n)
s  o(1) as graph array can be used as adj list 
'''


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        #vis1 vis2, keep nodes in path of node1 , node2 , respectively , and the dist from them 
        vis1 ,vis2 = {}, {}
        def dfs(node,vis, dist):

            if node ==-1 or  node in vis :

                return 

            vis[node] = dist
            
            neib = edges[node]
            dfs(neib,vis, dist+1)
        
        dfs(node1,vis1,0)
        dfs(node2,vis2,0)
      
        n = len( edges )
        ans   , minDist = float("inf"), float("inf")
        for i in range(n):
            #new minimised max found then store it in mindist and that is the ans node 
            if (i in vis1)  and( i in vis2):

                if max(vis1[i],vis2[i]) < minDist:
               
                    minDist = max( vis1[i],vis2[i])
                    ans  = i 

                #in case same minDist, take that node with less  value(index value) 
                    
                elif max(vis1[i],vis2[i]) == minDist:
                
                    ans  = min(ans , i)
        
        
        return  -1  if ans  == float("inf") else ans 