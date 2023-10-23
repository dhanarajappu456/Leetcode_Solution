class Solution:
    def isPowerOfThree(self, n: int) -> bool:


        '''
            we check max pow of 3 under 2**31-1
            since 3 is a prime  number ,  this max power can only be divided by  3 or its power
            which is what we check 
            
        '''
        if n<=0:
            return False
        maxPow3 = 1162261467

        return maxPow3 %n ==0

        