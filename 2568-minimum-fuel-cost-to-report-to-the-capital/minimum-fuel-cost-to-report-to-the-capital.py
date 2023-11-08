from collections import defaultdict as dict 

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # the same solution , 
        #we return the number of people reaching a node, and the fuel to reach the node  = 1*(number of cars reaching the node) =( number of people/seat)
        vis = set()
        adj = dict(list)
        for e in roads:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        fuel =[0]
        def rec(node):
            totPeople= 0
            vis.add(node)   
            for neib in adj[node]:
                if neib not in vis:
                    people = rec(neib)
                    #total fuel to reach from neib to node is =( no of cars travelling from neib to node)*1
                    fuel[0] += math.ceil(people/seats)
                    totPeople+=people
            totPeople += 1
            return totPeople


        rec(0)
        return fuel[0]




        