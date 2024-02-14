class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        n,m = len(text1),len (text2)
        memo = [[-1 for i in range(m+1)] for j in range(n+1)]
        def rec(ind1,ind2):
            if ind1==0 or ind2 ==0:
                return 0
            if memo[ind1][ind2]!=-1:
                return memo[ind1][ind2]
            if text1[ind1-1] == text2[ind2-1]:
                memo[ind1][ind2]   = 1+ rec(ind1-1,ind2-1)
            else:
                memo[ind1][ind2] = max(rec(ind1-1, ind2), rec(ind1, ind2-1))
            return memo[ind1][ind2]
        return rec(n,m)

            
            
            
        