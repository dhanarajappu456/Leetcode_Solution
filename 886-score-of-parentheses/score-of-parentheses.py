class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        
        for c in s:
            num = 0
            if c == "(":
                stk.append(c)
            elif c==")":
                current_open_matched = False
                item  = stk[-1]

                # if top is( pop it ansd push 1

                if  item=="(":
                    current_open_matched = True
                    num = 1
                    stk.pop()
                #if top was a number add all previosu number until ( 
                #and double this sum and insert to stack
                else:
        
                    while stk and stk[-1]!="(":
                        item = stk.pop()
                        num+=item
                    num*=2

                    stk.pop()
            
              
                stk.append(num)
        #at end stack  will have only numbers that need to be added
        return sum(stk)
            
     

        