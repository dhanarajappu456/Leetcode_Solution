#solution1 

'''
simulation 

t = logn
s= 1


'''

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while(n>1 ):


            if n%2 ==0:
                matches +=n//2
                n = n//2
            else:
                matches+= (n -1 )//2 
                n  = (n -1 )//2 +1

        return matches
        
'''
#solution 2 

observation 


n = 1 => ans 
n = 1 => ans 
n = 1 => ans 
t = 1
s= 1


'''