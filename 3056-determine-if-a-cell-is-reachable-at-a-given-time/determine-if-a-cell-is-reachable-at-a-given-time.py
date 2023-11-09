'''

solution 1 

bruteforce - using bfs  to calculate  mintime  and check if given time >= mintime

t n -tle
s n  - tle

solution 2 - optimised - finding  minTime(via diag cell and then moving either col or row) and check if time>= mintime
code of which is below 

t 1
s 1



solution 3 - same same as optimised - easy to code,

if u observe the min time to reach the cell fx and fy is max(horizontal dist and vert dist)
just check if given t>=mintime 

t 1
s 1
'''

#solution 3
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy ==fy:
            return t!=1 
        minTime = max(abs(sx-fx) , abs(sy-fy))
        return t>=minTime
        