import heapq as h 

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        #graph
        adj  = defaultdict(list)
        for a,b in edges: 
            adj[a].append(b)
            adj[b].append(a)

        def djikstras():
            #this keeps first min time, second min-time to reach to a node respectively. 
            d1,d2  = [float("inf") for i in range(n+1)], [float("inf") for i in range(n+1)]
            d1[1] = 0 
            min_heap = [(0,1)]
            while(min_heap): 
                cost, node = h.heappop(min_heap)
                #detrmining at what time we can reach the nbr , with the light green/red condn
                nb_cost = cost
                if  (cost//change)%2 == 1 :
                    nb_cost = ((cost//change)+1 )*change
                nb_cost += time
                for nb in adj[node]:
                    #filling up the d1[nb], which is the first min_value , 
                    #with which we can reach the nb
                    if d1[nb]==float("inf"):
                        d1[nb] = nb_cost
                        h.heappush(min_heap,(nb_cost,nb))
                    #filling up the d2[nb], which is the second min_value , 
                    #with which we can reach the nb,
                    #note that we can't  second min_value shouldn't be same as the
                    #first min_value , d1[nb]
                  
                    elif (d2[nb]==float("inf"))  and (nb_cost != d1[nb]): 
                        if nb  == n :
                            return nb_cost
                        d2[nb] = nb_cost
                        h.heappush(min_heap,(nb_cost,nb))
        return djikstras()

                        
                    



        