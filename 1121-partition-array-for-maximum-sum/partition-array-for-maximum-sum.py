'''
The idea is to use dp 

we use rec(i)-> which indicate max value we can get starting from i to end making parition with k elements in each partition 
at most
'''

from functools import lru_cache 

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        @lru_cache(None)
        def rec(i):

            if i==n:
                return 0
            print(i)
            max_ =0 
            k_ =0
            res = 0
            for j in range(i,min(n,i+k)):

                max_ = max(max_,arr[j])
                k_+=1
                res  = max(res, max_*k_ +rec(j+1))
            return res
        return rec(0)