class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        '''

        follow take not take approach of knapsack , with 3 states stored the ind,tot_profit earned so far, remaining number of people can be chosen

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