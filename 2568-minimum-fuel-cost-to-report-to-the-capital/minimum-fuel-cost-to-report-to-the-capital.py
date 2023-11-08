from collections import defaultdict as dict 

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        #it is a tree, so no cylce  and only one path  b/w each node
        #we start dfs from 0 
        #at any node, keep track of number of poeple reaching the node, based on which 
        #we determine , number of cars we might need  to travel ,up a dist(towrds 0) from the current node , we also need  
        #the totcars reaching a node, based on which we calulate the fuel needed to reach this node, just from a node below and adj to it , each node also keep a variable fuel , needed to reach that particular node
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
                    #all fuel to reach the neib node(fuelSofar,) + the fuel needed to reach node, from neib 
                    #which is nothing but totcars travelling from neib to node(each costing 1 litre of fuel)
                    fuel = fuel+  fuelSofar+(1*carsSofar)
            #for next node above, tot people increase by one including the currentnode(or representative as they said in the description)
            people = people+1
            #remeber , this is not clear from the description , 
            #actually the representatives from other cars reaching a node, can reorganise themselves, to minimise the number of cars used, that is fuels used(meaning unfilled cars from neib node below, can be utilsed by other people travellign in another unfilled car, so that extra cars can be dicarded , that is why we takes people /ceil)
            cars = math.ceil(people/seats)
            return (people, cars, fuel)
        
        people, cars, fuel = rec(0)
        return fuel




        