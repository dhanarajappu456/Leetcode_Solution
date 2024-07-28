class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        #graph creattion
        adj  = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)

        #normal bfs
        def bfs():
            q= deque([(1,0)])
            #maps the node and the two unique time values by which we reach it 
            vis_times = defaultdict(set)
            vis_times[1].add(0)
            while(q):
                node,nd_cost = q.popleft()
                #we should know at what time we would be able to pass out of node , as the ligh goes green and red 
                #nb_cost will store this time at which we will be allowed to move from the node to neib, in addition to the the edge cost "time"
                nb_cost  = nd_cost
                if (nd_cost//change)%2 ==1:
                    nb_cost  = ((nd_cost//change)+1)*change
                #adding the edge cost "time" as well
                nb_cost += time

                for nb in adj[node]:
                    #we will have to visit a node at max twice not more than that, and also not that 
                    #we want the second min to be unique from first min , there is no need to add the same cost to reach a particular node again ,
                    #as it gonna generate same values again for all nodes in its path
                    if ( (  len(vis_times[nb]) <=1 )  and (nb_cost not in vis_times[nb])   ):
                        vis_times[nb].add(nb_cost)
                        q.append((nb,nb_cost))
                    #when the nb is the node n , and we have  visited it twice, meanining that , we found the ans
                    if (nb ==n ) and (len( vis_times[nb]) ==2): 
                            return  nb_cost
            return -1
        ans = bfs()
        return ans
                    

                    

        