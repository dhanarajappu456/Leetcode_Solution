class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        '''

        optimised 

        follow take not take approach of knapsack , with 3 states stored the ind,tot_profit earned so far, remaining number of people can be chosen, but this time we try reducing the range of values ot totprofit , as this is what gave time and memory limit exceeded  

     

the only difference we keep an upper bound for total profti that it never cross the minprofit 

that is 
as we follow take not take , approach , when we cross minprofit we reduce it to the minprofit , as we bother about knowing if the amount collected is atleast minprofit , and not bothered about exact amount, 

thus the total profit constrained to 100 than 100*100 ( which case we got  time and memory limit exceeded)

        '''
        memo = {}
        mod   = 10**9+7
        def rec(ind, tot_profit, rem_members):

            if ind<0:
                
                if (tot_profit==minProfit):
                   
                    return 1
                return 0

            if (ind,tot_profit, rem_members) in memo:
                return memo[(ind, tot_profit , rem_members)]

            tk = 0
            if group[ind]<=rem_members:
                tk  = rec(ind-1,min(minProfit , tot_profit+profit[ind]),rem_members-group[ind])
            not_ = rec(ind-1,tot_profit, rem_members)
            memo[ (ind,tot_profit, rem_members)]= (tk%mod+not_%mod)%mod
            return memo[ (ind,tot_profit, rem_members)]

        m = len(profit)
        return rec(m-1, 0, n)
        
        '''

        t  profit*tot*profit*n = 100 *(100*100) *100
        s  profit*tot*profit*n = 100 *(100*100) *100

        '''