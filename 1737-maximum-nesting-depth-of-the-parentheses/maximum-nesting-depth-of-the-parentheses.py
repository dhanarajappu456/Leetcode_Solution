class Solution:
    def maxDepth(self, s: str) -> int:

        stk  =[]
        open = 0
        ans  = 0 
        for c in s:
            if c  =="(":
                open+=1
                ans = max(ans, open)
         
            elif c ==")":
                open-=1
            
            
        return ans 
        