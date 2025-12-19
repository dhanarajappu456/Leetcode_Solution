class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        #sliding window 
        #current profit with strategy being  whole 1 
        curr_profit = 0 
        #profit from index k to end
        inital_profit = 0
        #total profit with all the given strategy
        total_profit = 0
        n = len(prices)
        for i in range(n):
            if i>=k:
                inital_profit+=(prices[i] * strategy[i])
            total_profit += (prices[i] * strategy[i])
        
        n  = len(prices)
        #keeeps  track of profit  = prices * strategy
       
        curr_profit = inital_profit
        #all strategy from ind= k//2 to k-1 is 1 , so 
        for i in range(k//2,k):
            curr_profit += ( prices[i] * 1)
        
        #may be the initalu strategy would be the best one 
        # that is why sum(profit) also may be the ans
        ans = max ( curr_profit ,total_profit)
        i,j = 0 , k-1
        while(j<n):
            ans =max(ans,curr_profit)
            j+=1
            if j<n:
                # we  need to add the new price at j to the ans as sttrategy will be 1 now at j 
                #but before that we need to undo the effect of previous strategy that was at this index
                if strategy[j] ==1:
                    curr_profit -= prices[j]
                elif strategy[j]== -1:
                    curr_profit += prices[j]
                curr_profit+= prices[j]
                # the strategy at i+k//2 was 1 , intially, 
                # so we had taken the prices at i+k//2 , we need to undo it 
           
                curr_profit -= prices[i+k//2]
                #the strategy at  i was 0 , now we need to  consider the actual strategy that was there
                #at index i 
                if strategy[i] == 1:
                    curr_profit+= prices[i]
                elif strategy[i] == -1:
                    curr_profit-= prices[i]
                i+=1
            


                


        
        return ans


        