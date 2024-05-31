class Solution:
    def checkRecord(self, n: int) -> int:
        #memoisation -  but tle
        #t n*2*3 = n 
        #s   = n*2*3
        # mod = 10**9+7
        # memo = defaultdict(int)
        # def rec(i,a_cnt,l_cnt):
        #     if (a_cnt==2 ) or ( l_cnt == 3 ): 
        #         return 0

        #     if i == n :
        #         return 1 
            
        #     if (i,a_cnt,l_cnt) in memo:
        #         return memo[(i,a_cnt,l_cnt)]

        #     a = rec(i+1,a_cnt+1,0)%mod
        #     l = rec(i+1,a_cnt,l_cnt+1)%mod
        #     p =  rec(i+1,a_cnt,0)%mod

        #     memo[(i,a_cnt,l_cnt)] =  (a+p+l)%mod
        #     return  memo[(i,a_cnt,l_cnt)] 

        #     return rec(0,0,0)

        #dp - 
        #t n*2*3 = n 
        #s   = n*2*3
        mod = 10**9+7
        dp =[ [[0 for i in range(4) ] for j in range(3)  ] for k in range(n+1)]
        for i in range(3):
            for j in range(4):
                if i!=2 and j !=3:
                    dp[n][i][j] =1 
        for i in range(n-1,-1,-1):
            for a in range(1,-1,-1):
                for l in range(2,-1,-1):

                    a_tk = (dp[i+1][a+1][0])%mod

                    l_tk  = (dp[i+1][a][l+1])%mod
                    p_tk =( dp[i+1][a][0])%mod
                    dp[i][a][l] = (a_tk + l_tk + p_tk)%mod
        return dp[0][0][0]



        # for i in range(n-1,-1,-1):
        return 8