'''
solution1 
memo 

the idea is rec(l,h) -> stores the minium ans for array ranging from l,h

t n^3 
s  n(aux) + n^2(memo ds )

'''

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        @lru_cache(None)
        def rec(l,h):
            if l>=h:
                return 0
            ans = float("inf")
            for k in range(l,h):
                val = max(arr[l:k+1]) * max(arr[k+1:h+1])  + rec(l,k) + rec(k+1,h)
                ans  = min(val,ans)
            return ans
        n = len(arr)
        return rec(0,n-1)
        