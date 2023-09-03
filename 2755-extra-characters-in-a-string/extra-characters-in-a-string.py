class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n = len(s)
        @lru_cache(None)
        
        def rec(i):
            if  i == n:
                return 0 
            ans  = float(inf)
            for  j in range(i,n):

                if s[i:j+1] not in dictionary:
                    ans = min( ans , (j-i+1) + rec(j+1))
                else:
                  
                    ans   = min( ans , rec(j+1)) 
            return ans 
        return rec(0)
        