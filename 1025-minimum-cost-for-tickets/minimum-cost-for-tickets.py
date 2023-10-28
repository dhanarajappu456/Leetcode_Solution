
from collections import defaultdict as dict
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:


        n = len(days)
        memo = dict(int)
        def rec(ind,d):

            if ind  ==n:
                return 0 
            if (ind,d) in memo:
                return memo[(ind,d)]

            if days[ind]<=d:
                memo[(ind,d)]  = rec(ind+1,d)
            else:

                 memo[(ind,d)] =  min(

                    costs[0]+  rec(ind+1,days[ind]),
                    costs[1] + rec(ind+1, days[ind]+ 6),
                    costs[2] + rec(ind+1,days[ind]+29)
                )
            return memo[(ind,d)]
        return rec(0,0)