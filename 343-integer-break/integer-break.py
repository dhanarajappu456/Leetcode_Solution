
#idea is simple we check all possibility of numbers i  possible to be splitted for num , ie, from(1 to num -1 )


#then recursively call the function for (num-i)



class Solution:
   
    def integerBreak(self, n: int) -> int:
        
        # memo = {}
        # def rec(n):
            
        #     if n==0:
        #         return 0 
        #     if n ==1:
        #         return 1

        #     if n in memo:
        #         return memo[n]

        #     ans  =  0 
        #     for i in range(1,n+1):

        #         ans  = max(ans, i*max(n-i, rec(n-i)))
        #     memo[n] =  ans
        #     return memo[n] 
        # return rec(n)

    
        dp =[0 for i in range(n+1)]
        dp[1] =1 
        for i in range(2,n+1):
            ans  =  0 
            for j in range(1,i+1):
                ans  = max(ans, j*max(i-j, dp[i-j]))
            dp[i] =  ans
        return dp[n]


