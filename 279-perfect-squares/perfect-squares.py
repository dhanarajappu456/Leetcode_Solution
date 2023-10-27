
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
            elif num<0:
                return float("inf")
            if memo[num]!=-1:
                return memo[num ]
            ans = float("inf")
            for i in range(1,int(math.sqrt(num))+1):
                sqr = i*i
                ans = min(ans, 1+rec(num-sqr)) 
            memo[num ] =  ans
            return memo[num ]

        return rec(n)


