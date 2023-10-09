class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        

        m,n  = len(word1) , len(word2)
        @lru_cache(None)
        def rec(i,j):

            if i<0 or j<0:
                return 0
            elif word1[i] == word2[j]:

                return  1+rec(i-1, j-1)
        
            return max(rec(i-1, j) , rec(i,j-1))
    
        return m+n-2*rec(m-1,n-1)