# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random 
class Solution:
    def rand10(self):
        
        while(True):
            r = random.randint(1,6)
            c = random.randint(1,7)
            val = (r-1)*7+c
            if val<=40:
                break
        
        ans = val%10
        if ans ==0:
            return   10
        return ans

        
        
        