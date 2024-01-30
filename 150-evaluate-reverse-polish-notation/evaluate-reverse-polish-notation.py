class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator  = {"*","/","+","-"}
        stk  = []
        for c in tokens:
            if c in operator:
                
                a =stk.pop()
                b =stk.pop()

                if c ==  "+":
                    stk.append(b+a)
                elif c =="-":
                    stk.append(b-a)
                elif c =="/":
                    stk.append(int((b/a)))
                    
                else:
                    stk.append(b*a)

            else:
                stk.append(int(c))
        return stk[-1]