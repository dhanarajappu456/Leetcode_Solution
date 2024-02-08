
'''

with each number brute force with all the perfect sqaure less than that number , and see which path gives min number of 
elements
'''

class Solution:
    def numSquares(self, n: int) -> int:
        memo = [-1 for i in range(n+1)]


        def rec(num):

            if  num ==0:
                return 0
            if memo[num]!=-1:
                return memo[num ]
            ans = float("inf")
            for i in range(1,int(math.sqrt(num))+1):
                sqr = i*i
                ans = min(ans, 1+rec(num-sqr)) 
            memo[num ] =  ans
            return memo[num ]

        return rec(n)
        # num = n
        # dp = [0 for i in range(num+1)]
        # for num in range (1,num+1):
        #     ans = float("inf")
        #     for i in range(1,int(math.sqrt(num))+1):
        #         sqr  = i*i
        #         if num-sqr<0:
        #             break
        #         ans = min(ans,1+dp[num-sqr])
        #     dp[num] = ans
        # return dp[num]





