#solution 1 - with stk and deq , greedey 
from collections import deque 

class Solution:
    def checkValidString(self, s: str) -> bool:
      
        #a deq is needed here as 
        #1)popleft
        # when we see a ) , we need to see if we have * seen already 
        #where we store the stars in fifo , and need to pop the * assuming it as (
        #2) At the end of the for loop the stk might contain open brackets, which can be 
        #mapped to * assuming as )
        #so we need to popright in deq 
        deq= deque([])

        stk = []
        for i,c in enumerate(s) :
            if c == "(":
                #index info needed to see if in case c  = ")"
                # and we need to know if the * comes before it so that it can be assumed as (
                stk.append((i,"(",))
            elif c == ")":
                #direct pop if there isopening bracket seen so far
                if stk and stk[-1][1] == "(":
                    stk.pop(-1)
                #assuming * as (
                elif deq:
                    deq.popleft()
                else:
    
                    return False
            #add the *  to deq
            else:
                deq.append(i)
        # now the stack will only have (
        # so we need to match it with * assuming as )
        #where we need to do popleft in deq
        while(stk):
            #check if the * comes after the (, then only it can be matched
            if  stk and  deq and deq[-1]>stk[-1][0]:
                stk.pop(-1)
                deq.pop()
     
            else:
                return False
           
        
        return True

    #t n 
    # s n 



