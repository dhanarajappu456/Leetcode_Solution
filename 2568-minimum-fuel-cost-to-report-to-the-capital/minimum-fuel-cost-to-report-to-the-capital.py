from collections import defaultdict as dict 

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        #at any node, keep track of number of poeple reaching the node, based on which 
        #we determine , number of cars we might need , which my travel up costing 1*number of cars fuel

        vis = set()
        adj = dict(list)
        for e in roads:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
  
        def rec(node):

            
            people, cars, fuel = 0,0,0
            vis.add(node)   
            
            for neib in adj[node]:
                if neib not in vis:

                    peopleSofar , carsSofar , fuelSofar = rec(neib)
                    people+=peopleSofar
                    cars+=carsSofar
                    fuel = fuel+  fuelSofar+(1*carsSofar)
                   
            people = people+1
            cars = math.ceil(people/seats)
            fuel  = fuel 
            return (people, cars, fuel)
        
        people, cars, fuel = rec(0)
        return fuel




        