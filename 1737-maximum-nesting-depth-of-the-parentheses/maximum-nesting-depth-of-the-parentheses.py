class Solution:
    def maxDepth(self, s: str) -> int:

        stk  =[]
     
        ans  = 0 
        for c in s:
            if c  =="(":
        
                stk.append(c)
            #it is is said s is vps , so the parenthesis will be such that they match and 
            #is balanced, so for closing bracket an open bracket will be there for sure
            elif c ==")":
  
                stk.pop(-1)
            ans = max(ans , len(stk))
            
        return ans 
        