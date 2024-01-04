from functools import lru_cache

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        

        @lru_cache(None)
        def dfs(count):
            if count ==0:
                return 0
            if count ==1:
                return float("inf")
            elif count ==2:
                return 1

            
            else:
                return 1+min(dfs(count-2), dfs(count-3))
            
        m =Counter(nums)
        ans  =0 
        for num in m:
            min_op = dfs(m[num])
            if min_op == float("inf"):
                return -1
            ans+= min_op
        return ans
        
       
    

            
        