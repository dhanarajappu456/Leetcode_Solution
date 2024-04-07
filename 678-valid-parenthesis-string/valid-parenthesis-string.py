
from collections import deque 

class Solution:
    def checkValidString(self, s: str) -> bool:
      

        deq= deque([])

        stk = []
        for i,c in enumerate(s) :
            if c == "(":
                stk.append((i,"(",))
            elif c == ")":
                if stk and stk[-1][1] == "(":
                    stk.pop(-1)
              
                elif deq:
                    deq.popleft()
                else:
    
                    return False
            else:
                deq.append(i)
      
        while(stk):
            
            if  stk and  deq and deq[-1]>stk[-1][0]:
                stk.pop(-1)
                deq.pop()
     
            else:
                return False
           
        
        return True



