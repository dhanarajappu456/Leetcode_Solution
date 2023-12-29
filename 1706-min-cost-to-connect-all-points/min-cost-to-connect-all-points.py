
'''
#solution 1 - greedy - mimicking like prims algo(but without minheap)
the idea is simple , we aim to connect the remaining points(means unconnected points) to the any of the points in the set of points in the component 

HOW IT WORKS? 


1)we choose a parentpoint( a point recently added or joined with the componenet ) - to calculate the dist of all unconnected points from it. and update the dist  array for each point i , if it is a new minimum 

what is  a dist array - has ?

where dist[i] is the min dist of the point i , from all other points in the connected component.

at the end of inner for loop dist[i] has min  distance of point i , from all the points in the connect component , including the parentpoint(lastly added to component).

So it is all about selecting a unconnected point , which is that point with min dist value in the dist array  and added to the component 

now this added point component becomes parentpoint from which we need to calculate distance of all other points, updating it, if it is minimum than min so far in the dist array



this is repeated till we get n-1 time(that is = number of edges )

we can also apply prims or kruskal algo in this, 
the given approarch mimic prim's algo in a fashion
t n^2 , n= number of vertivces
s n

'''




class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        def manhattan( p1, p2) :
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        connected_points  = set()
        tot_cost = 0 
        par_point_ind = 0
        n = len(points)
        dist =[float("inf") for i in range(n)]
        for edges in range(n-1):
            
            connected_points.add(par_point_ind)

            for i in range(n):
                if i!=par_point_ind:
                    dist[i] =min(dist[i] , manhattan(points[par_point_ind], points[i]))
            edge_min_dist = float("inf")
            point_ind = None
            for i in range(n):

                if (i not in connected_points ) and  (dist[i]<edge_min_dist):
                        point_ind = i
                        edge_min_dist =dist[i]
            tot_cost  += edge_min_dist

            par_point_ind  = point_ind

        return tot_cost
        