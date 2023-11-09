'''

solution 1 

bruteforce - using bfs  to calculate  mintime  and check if given time >= mintime

t n -tle
s n  - tle

solution 2 - optimised - finding  minTime(via diag cell and then moving either col or row) and check if time>= mintime
code of which is below 

t 1
s 1



solution 3 - ssame same as optimised ,

if u observe the min time to reach the cell fx and fy is max(horizontal dist and vert dist)
just check if given t>=mintime 

t 1
s 1
'''

#solution 2
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy ==fy:
            return t!=1 
        numberofDiagToTravel  = min(abs(sx-fx),abs(sy-fy))
      
        minTime = numberofDiagToTravel 
        coordSign  ={1:(-1,-1),2:(1,-1),3:(1,1),4:(-1,1)}
        #the diagonal cell travelled would be differnt based on relative position of start and end cell , 
        #so we see in which qudrant the dest cell lie wrt ot start cell, based on which sign 
        qdr =None

        #     1   |   2 
        #         |
        # ___________________
        
        #     4   |   3
        #         |
                
        if fx<=sx and fy<=sy:
            qdr = 1
        elif fx>=sx and fy<=sy:
            qdr = 2
        elif fx>=sx and fy>=sy:
            qdr = 3 
        else:
            qdr = 4
       
        newX   = sx+coordSign[qdr][0]*numberofDiagToTravel
        newY =   sy+ coordSign[qdr][1] *numberofDiagToTravel
    
        minTime+= abs(newX-fx) + abs(newY-fy)         
        
        return t>=minTime
        