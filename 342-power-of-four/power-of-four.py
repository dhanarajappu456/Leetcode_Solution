class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''

        any num which is power  of 4 has property , 
        1) it is power of 2  and
        2) num-1 is mul(3)

        '''
        
        if n<=0: 
            return False

        return  n&(n-1 ) ==0   and (n-1)%3==0

        

    
        