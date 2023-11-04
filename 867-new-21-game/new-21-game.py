class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        #approach1 - ree / memoisation 
        # @lru_cache(None)
        # def rec(score):
            
        #     if score>=k:
        #         return 1 if score<=n else 0 
                    
        #     ans  = 0
        #     for i in range(1,maxPts+1):
              
        #         ans  += rec(score+i)
        # #probabilty must be divided by 1/maxpts
        #     return ans/maxPts
        # return rec(0)

        # approach 2 - dp of memoised code, - but opmtisation of inner loop with sliding window 
      

        dp = [0 for i in range(k+maxPts)]
        for i in range(k,min(n+1 ,len(dp))):
            dp[i]=1
        
        i,j = k, k+maxPts-1
        winSum = sum(dp[i:j+1])
        sum_  = winSum 
        for p in range(k-1,-1,-1):
            dp[p] = 1/maxPts*(sum_)
            sum_  = sum_- dp[j] + dp[p]
            j -=1
        return dp[0]


    




        

