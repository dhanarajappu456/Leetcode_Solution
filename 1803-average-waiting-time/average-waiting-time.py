class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        prev_complete  = customers[0][0]
        wt =  0
        n = len(customers)
        for i in range(n):
            arrive,process = customers[i][0],customers[i][1]
            complete  =  max(arrive+process, prev_complete+process)
            wt += complete - arrive
            prev_complete = complete

        return wt/n

        