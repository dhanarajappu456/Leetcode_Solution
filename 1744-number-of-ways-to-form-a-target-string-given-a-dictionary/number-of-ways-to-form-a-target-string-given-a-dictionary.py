from collections import defaultdict as dict 

class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        n= len(words[0])
        freq = dict(int)
        for i in range(n):

            for w in words:

                c = w[i]

                freq[(i,c)]+=1
        print(freq)

        memo = { }
        mod = 10**9+7
        def rec(i,j):

            if j<0:
                return 1
            elif i<0:
                return 0

            if (i,j) in memo:
                return memo[(i,j)] 
            ans = 0
            
            target_char = target[j]
            #match curr character of target , with corresponding char   ith position of across  all  words 
            ans = (ans+(freq[(i,target_char)]*rec(i-1, j-1)%mod))%mod
            #skip  matching the character 
            ans = (ans + rec(i-1,j)%mod)%mod
            memo[(i,j)] = ans%mod
            return memo[(i,j)]
        t= len(target)
        return rec(n-1, t-1)

            





        