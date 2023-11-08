class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy ==fy:
            return t!=1 
        numberofDiag  = min(abs(sx-fx),abs(sy-fy))
        minTime =0
        minTime+= numberofDiag
        coord  ={1:(-minTime,-minTime),2:(minTime,-minTime),3:(minTime,minTime),4:(-minTime,minTime)}
        
        coordinate =None
        if fx<=sx and fy<=sy:
            coordinate = 1
        elif fx>=sx and fy<=sy:
            coordinate = 2
        elif fx>=sx and fy>=sy:
            coordinate = 3 
        else:
            coordinate = 4
       
        newX,newY  = sx+coord[coordinate][0],sy+ coord[coordinate][1]
    
        minTime+= abs(newX-fx) + abs(newY-fy)         
        
        return t>=minTime
        