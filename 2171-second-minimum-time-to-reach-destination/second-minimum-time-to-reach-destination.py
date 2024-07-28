import heapq as h 

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adj  = defaultdict(list)

        for a,b in edges: 

            adj[a].append(b)
            adj[b].append(a)

        def djikstras():
            d1,d2  = [float("inf") for i in range(n+1)], [float("inf") for i in range(n+1)]
            d1[1] = 0 
            min_heap = [(0,1)]

            while(min_heap): 
                cost, node = h.heappop(min_heap)
                nb_cost = cost
                if  (cost//change)%2 == 1 :
                    nb_cost = ((cost//change)+1 )*change
                nb_cost += time
                for nb in adj[node]:
                    
                    if d1[nb]==float("inf"):
                        d1[nb] = nb_cost
                        h.heappush(min_heap,(nb_cost,nb))
                    elif (d2[nb]==float("inf"))  and (nb_cost != d1[nb]): 
                        if nb  == n :
                            return nb_cost
                        d2[nb] = nb_cost
                        h.heappush(min_heap,(nb_cost,nb))
        return djikstras()

                        
                    



        