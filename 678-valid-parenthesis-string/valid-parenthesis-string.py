#solution 1 - with 2 stack , greedey 
from collections import deque 

class Solution:
    def checkValidString(self, s: str) -> bool:
      
        '''
        we use 2 stack , one for pushing the  parenth
        other for aster

        when we find there is not mathching open par in stack for a closed par
        we check if aster stack has one, which can be assumed as open par

        at end of loop , the par stack has only open pars, so 
        we need to check if asterisk stack has aserisks, which can be assumed as closed pars

        t n 
        s n

        '''
        aster_stk= []
        par_stk = []
        for i,c in enumerate(s) :
            if c == "(":
                #index is needed when matching open pars in stack to asterisk as closed pars
                #at the end of the for loop, where asterisk can be taken as closed pars, iff it comes after the open 
                #pars
                par_stk.append((i,"("))
            elif c == ")":
                #direct pop if there is opening bracket seen so far
                if par_stk and par_stk[-1][1] == "(":
                    par_stk.pop(-1)
                #assuming * as (
                elif aster_stk:
                    aster_stk.pop(-1)
                else:
    
                    return False
            #add the *  to deq
            else:
                aster_stk.append(i)
        # now the stack will only have (
        # so we need to match it with * assuming as )
        #where we need to pop asterisk from aster stack which can be assumed as 
        #) , if it comes after this open par 

        while(par_stk):
            #check if the * comes after the (, then only it can be matched
            if  par_stk and  aster_stk and aster_stk[-1]>par_stk[-1][0]:
                par_stk.pop(-1)
                aster_stk.pop(-1)
     
            else:
                return False
           
        
        return True

    #t n 
    # s n 



