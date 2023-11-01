class Solution:
    def maxProfit(self, prices: List[int]) -> int:

     
        n   =len(prices)
        dp =[[0,0] for i in range(n+2)]
        for i in range(n-1,-1,-1):
            #max cost from  i to end , when the flag is buy at i, 
            dp[i][0] = max(-prices[i]+dp[i+1][1],dp[i+1][0])
            #max cost from  i to end , when the flag is sell at i, 
            dp[i][1] = max(prices[i]+ dp[i+2][0], dp[i+1][1])  
           

        return dp[i][0] 
        