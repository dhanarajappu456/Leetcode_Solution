class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        curr_profit = 0 
        n  = len(prices)
        profit =  [ prices[i] * strategy[i] for  i in range(n)]
        curr_profit = sum(profit[k:])
      
        for i in range(k//2,k):
            curr_profit += ( prices[i] * 1)
      
        ans = max ( curr_profit , sum(profit))
        #print(profit,curr_profit,sum(profit),ans)

        i,j = 0 , k-1
        
    
        while(j<n):
            #print(curr_profit)
            ans =max(ans,curr_profit)
        
            #logic of what need to be done with element at j
            #logic for what need to be done with element at i+k//2
            

            j+=1
           

            if j<n:
                if strategy[j] ==1:
                    curr_profit -= prices[j]
                elif strategy[j]== -1:
                    curr_profit += prices[j]
                #print("cr1",j,curr_profit)
                curr_profit+= prices[j]
                #print("cr",j,curr_profit)
                # if k!=2:
                # if strategy[i+k//2] == -1:
                #     curr_profit += prices[i+k//2]
                # elif strategy[i+k//2] == 1:
                curr_profit -= prices[i+k//2]
                #print("cr",curr_profit)
            
                if strategy[i] == 1:
                    curr_profit+= prices[i]
                elif strategy[i] == -1:
                    curr_profit-= prices[i]
                
                #print("cr",curr_profit)


                i+=1


                


        
        return ans


        