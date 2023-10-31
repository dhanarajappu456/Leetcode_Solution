class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        # res = 1
        # for i in range(n):
        #     res = res * (2*i + 1) * (i + 1) % MOD
        # return res

        # @lru_cache(None)
        # def rec(p,d):

        #     if p==0:
        #         return math.factorial(d)
            

        #     ans = 0 

        #     for i in range(1,p+1):
        #         ans = (ans%MOD+ rec(p-1,d)%MOD)%MOD
            

        #     for i in range(1,d-p+1):
        #         ans = (ans%MOD+ rec(p,d-1)%MOD)%MOD
        #     return ans
        # return  rec(n,n)%MOD


        MOD = 10**9 + 7

        # Initialize the memoization table with 1 as the base case.
        memo = [1] * (n + 1)

        for i in range(2, n + 1):
            spaces =  2*(i-1)+1
            currPossibility = spaces*(spaces+1)//2
            
            prevPossibility  = memo[i-1]

            memo[i] = (prevPossibility*currPossibility) % MOD

        return memo[n]
