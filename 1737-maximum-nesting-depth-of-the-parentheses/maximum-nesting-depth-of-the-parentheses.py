class Solution:
    def maxDepth(self, s: str) -> int:
        #keeps track of open pars at any time
        open = 0
        ans  = 0 
        for c in s:
            if c  =="(":
                open+=1
            #it is is said s is vps , so the parenthesis will be such that they match and 
            #is balanced, so for closing bracket an open bracket will be there for sure
            elif c ==")":
                open-=1
            ans  = max(ans, open)
            
        return ans 
        