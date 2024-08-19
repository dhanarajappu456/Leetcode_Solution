class Solution:
    def minSteps(self, n: int) -> int:
        #dp[i] stotres the number of min operation to print i number of a's on screen
        dp  = [ float("inf") for i in range (n+1)]


        dp[0]  = 0 
        dp[1] = 0 
        
        #filling up dp in bottom up 
        for i in range(2,n+1):
            #when filling dp[i],
            #we need to see factors(fact_i) of  the number of a's to be printed  (i), 
            #so taht we can replicate fact_i number of a's till w get n number of a's 
            for fact_i in range(1,i//2 + 1):
                if i % fact_i ==0 :
                    #when fact_i is factor of i( i is the number of a's currently on screem)
                    #we replicate it i // fact_i -1 times ,  so that we get n a's
                    #total operation  = 
                    #numer of opeation to get to i number of a's + 1 (copying i nuber of a's)  + i // fact_i -1
                    #(pasting it i // fact_i -1 times)
                    dp[i] = min (dp[i], dp[fact_i] + (1 + i // fact_i -1)) 
        return dp[n]
        