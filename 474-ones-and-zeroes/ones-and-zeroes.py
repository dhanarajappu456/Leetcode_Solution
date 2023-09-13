class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:


        l = len(strs)

        @lru_cache(None)
        def rec(i,m,n):

            if i == l:
                return 0

            s = strs[i]
            tk = -1
            if m>=s.count("0") and n>= s.count("1"):

                tk = 1+ rec(i+1,m-s.count("0"),n-s.count("1"))
            not_tak = rec(i+1,m,n)
            ans = max(tk,not_tak)

            return ans
        
        return rec(0,m,n)
        