

from collections import defaultdict as dict 
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def rec(length):

            if length >high: 
                return 0
            
            ans =(rec(length+zero)%mod + rec(length+one)%mod)%mod

            if length>=low:
                 return( 1+ ans)%mod
            else:
                return ans 
        return rec(0)