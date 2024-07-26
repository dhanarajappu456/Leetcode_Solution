import heapq as h 

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        adj = defaultdict(list)
        for a,b,w in edges:

            adj[a].append((b,w))
            adj[b].append((a,w))

        def djikstra(i):

            d =[float("inf") for i  in range(n)]
            d[i] =0
            min_heap = [(i,0)]
            h.heapify(min_heap )
            #stores all nodes reachable from the source node
            #note , it is a set , since same nodes can be oushed to heap sometimes
            # ex: conider source 1
            # 1->(4,10) , (2,1)
            # 2->(4,1)
            #threshold :100
            # 4 may be pushed twice , here , but we need to have it only once
            nodes  =set()
            while(min_heap):
                node,w = h.heappop(min_heap)
                for nb,nb_wt in adj[node]:
                    #when the path len<=threshold and is reaching the nb with short path , update the valeu for nb 
                    #and include it to the st of reachable node
                    if (w+nb_wt<= distanceThreshold) and (d[nb]>w+ nb_wt):
                        h.heappush(min_heap , (nb,nb_wt+w))
                        d[nb] = w + nb_wt 
                        nodes.add(nb)
            return nodes

        ans  = -1 
        min_cnt  = float("inf")
        #for each node as source find all possible dest that can be reached
        for i in range(n):
            
            nodes  =  djikstra(i)
            if len(nodes) <= min_cnt:
                min_cnt = len(nodes)
                ans = i


        return ans


            



        