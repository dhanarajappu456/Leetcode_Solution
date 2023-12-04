

'''
Example - 1

the solution is simple , that , we try the bruteforce backtracking way of 

partitioning the  word 


t:


one way to code this is take or not take pattern wher we need 


curr ind, prev val and prev part index, as the paramter passed

where we make a partition at current index,  or not make partition at current index, 

so time = 2^n  = 2^20 = 10^6

s = n 

'''


class Solution:
    def splitString(self, s: str) -> bool:
        @lru_cache(None)
        def helper(prev, s):
            if not s:
                return True
            
            for i in range(1, len(s)+1):
                x = int(s[:i])

                if prev - x == 1:
                    if helper(x, s[i:]):
                        return True
            
            return False
        
        for i in range(1, len(s)):
            if helper(int(s[:i]), s[i:]):
                return True
        
        return False





                