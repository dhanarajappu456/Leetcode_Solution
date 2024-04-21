class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        
        for c in s:
            
            if c == "(":
                stk.append(c)
            elif c==")":
                if  stk[-1]!="(":
                    s = 0
                    while(stk and stk[-1]!="("):
                        num = stk.pop(-1)
                        s+= num
                    s*=2
                    stk.pop(-1)
                    stk.append(s)
                else:
                    stk.pop(-1)
                    s = 0
                    while(stk and ( stk[-1] != "(") ):
                          num = stk.pop(-1)
                          s += num
                    s+=1
                    stk.append(s)    
                #print(stk)
                          
        return sum(stk)
            
     

        