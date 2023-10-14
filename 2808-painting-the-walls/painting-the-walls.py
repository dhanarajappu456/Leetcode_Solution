'''


2d approach 


we only need to keep track of walls painted by the paid worker



we follow take not take approach ,

we use 2 state ind, remaining , which indicate min cost paint all the walls from ind to end ,  where "remaining " number of walls are there





t n^2 =  n = len (cost or time)
s  n^2
'''


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        n  = len(cost)
        memo ={}
        
        def rec(ind,remain_walls):

            if remain_walls <0:
                return 0 
            if n ==ind: 
               return float("inf")
            
            if (ind, remain_walls ) in memo:
                return  memo[(ind,remain_walls )] 

            tk   = cost[ind]+  rec(ind+1, remain_walls-time[ind]-1)
            not_ = rec(ind+1  ,remain_walls)

            memo[(ind,remain_walls )]  =  min(tk,not_)
            return  memo[(ind,remain_walls )] 
        return rec(0, n-1)
