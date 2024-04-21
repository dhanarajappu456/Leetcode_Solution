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

                # if top is (, just we would might need to push 1 to stack not immediately , keep it stored
                #in num , beacuse next top will be a number in which it need to be added to num and push this num

                if  item=="(":
                    current_open_matched = True
                    num = 1
                    stk.pop()
                #if top was a number double it 
                
                else:
        
                    while stk and stk[-1]!="(":
                        item = stk.pop()
                        num+=item
                    num*=2

                    stk.pop()
            
              
                stk.append(num)
      
        return sum(stk)
            
     

        