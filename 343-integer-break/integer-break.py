
#idea is simple we check all possibility of numbers i  possible to be splitted for num , ie, from(1 to num)



#when we split a number , to i and n-i, either i*(n-i) willbe max or n-i might be further broken(call recursion )

#as this is overlapping subproblem , we cache the result



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
        '''
        t num^2
        s : num 
        '''


