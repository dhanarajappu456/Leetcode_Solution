class Solution:
    def reverseParentheses(self, s: str) -> str:


        stk = []

        for c in s:

            if c=="(":
                stk.append(c)
            
            elif c == ")":
                str_ =""
                while(stk and stk[-1]!="("):
                    c = stk.pop()
                    str_ = c+str_
                str_=  str_[::-1]
                stk.pop()
                stk.append(str_)
                
            else: 
                stk.append(c)
        
        return "".join(stk)
        