'''


use the state (ind, days) ->indicate min code to travel all the days in array from ind to end, with days number of days i can cover still
'''
from collections import defaultdict as dict
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:


        n = len(days)
        memo = dict(int)
        daysList = [1,7,30]
        tickets = list(zip(costs, daysList))
        def rec(ind): #runs n times 

            if ind  ==n:
                return 0 
            if  ind  in memo:
                return memo[ind]
        
            ans = float("inf")
            #for each ticket, see how many days you 
            #can travel from the current index and call recursively for next day which you cant suffice with 
            #the ticket
            for cost,day_can_travel in tickets: # for loop and while together runs for,  1  + 7+ 230 = 38 times

                i = ind
                while(i<n and days[i]<=days[ind]+day_can_travel-1 ):

                    i+=1
                ans = min(ans, cost+ rec(i))
            memo[ind] = ans
            return ans
        return rec(0)

        t: n + 38 = 365 *38
        s: n  + aux
