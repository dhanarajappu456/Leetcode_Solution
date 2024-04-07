#solution 1 - recursion memo


class Solution:
    def checkValidString(self, s: str) -> bool:
      
        '''
        recursion memo

        t n^2
        s n^2(memo) + n(stk space)

        '''
        aster_stk= []
        par_stk = []
        n = len(s)
        @lru_cache(None)
        def rec(ind, open):
            if ind==n:
                return open == 0
            if s[ind] == "(":
                return rec(ind+1,open+1)
            elif s[ind] ==")":
                if open>0 : 
                    return rec(ind +1, open-1)
            else:
                ans  = rec(ind+1, open+1) or rec(ind+1,open) 
                if open>0:
                  ans = ans or rec(ind+1, open -1)
                return ans
        return rec(0,0)

    # t n^2
    #s n^2(memo) + n(stk space)


