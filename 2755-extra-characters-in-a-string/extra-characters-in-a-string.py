class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n = len(s)
        @lru_cache(None)
    
        def rec(start):


            if start ==n:
                return 0 

            ans = n
            for end in range(start,n):

                if s[start:end+1] in dictionary:
                    ans = min(ans ,  rec(end+1))
                else:

                    ans = min(ans, end-start+1 +  rec(end+1))
            return ans

        return rec(0)
    
        