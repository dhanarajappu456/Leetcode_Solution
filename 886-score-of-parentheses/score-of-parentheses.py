class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        
        for c in s:
            
            if c == "(":
                stk.append(c)
            elif c==")":
                item = stk.pop()
                if  item=="(":
                    num = 1
                else:
                    num = item*2
                if stk and stk[-1]!="(":
                    item = stk.pop()
                    num+=item
                else:
                    if stk:
                        stk.pop()
                stk.append(num)
        return stk[0]
            
     

        