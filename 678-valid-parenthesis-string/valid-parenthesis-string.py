#solution 3 - with 2 iteration from front and end
from collections import deque 

class Solution:
    def checkValidString(self, s: str) -> bool:
      
        '''
        1)iterating from start and we sum up total opens , 
        with aster being taken as open 
        during this , if open becomes <0 return False
        essentially we check , if there are sufficient opens for closed pars

        2)iterating from end  and we sum up total closed , 
        with aster being taken as closed 
        during this , if closed becomes <0 return False
        essentially we check , if there are sufficient closed pars for open pars
        t n 
        s 1

        '''
        close,open  = 0,0
        for c in s :
            if c ==")": 
                open-=1
            else:
                open+=1
            
            if open<0:
                return False

        
        for c in s[::-1]:
            if c =="(": 
                close-=1
            else:
                close+=1
            if close<0:
                return False
        return True
    #t n 
    # s n 


