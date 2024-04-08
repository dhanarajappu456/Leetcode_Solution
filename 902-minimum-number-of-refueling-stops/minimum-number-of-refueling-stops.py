#solution 1 - dp

'''
since there are choices for the pumps chosen when at index i, we can have 2 dimension dp 
dp[i][j] indicate the max dist that can travel , with  all i pumps  and out of which , j pumps  being chosen

t n^2
s n^2
'''

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        n = len(stations)
        dp  =[[0 for j in range(n+1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = startFuel

        
        for i in range(1,n+1):
            for j in range(1,i+1):
                #not choose the ith pump
                dp[i][j] = dp[i-1][j]
                #choose the ith pump
                if dp[i-1][j-1]>=stations[i-1][0]:
                    dp[i][j]  = max(dp[i-1][j], dp[i-1][j-1]+stations[i-1][1])

        #last row is the max dist can go , considering all n pumps
        #so ,just go through this row to get first col which has value maxdist >=target
        for j in range(n+1):
            if dp[n][j]>=target:
                return j
        return -1

            





