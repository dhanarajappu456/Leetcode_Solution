class Solution:
    def maxDepth(self, s: str) -> int:

        stk  =[]
        open = 0
        ans  = 0 
        for c in s:
            if c  =="(":
                open+=1
                ans = max(ans, open)
                stk.append(c)
            elif c ==")":
                open-=1
                stk.pop(-1)
            
        return ans 
        