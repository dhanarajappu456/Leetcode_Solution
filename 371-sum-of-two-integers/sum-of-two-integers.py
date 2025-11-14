class Solution:
    def getSum(self, a: int, b: int) -> int: 
        #12 bit mask
        mask = 0b111111111111
        while(b & mask):
            temp = a^b
            carry = (a&b)<<1
            a = temp
            b = carry
        # 1. if a is unsinged , return the number as such( but remebere we care about
        #only 11 bits)
        # 2. else, we return  = -2**12 + unsigned of this number 
        #which is the actual -ve numebr represented by this binary form
        return a & mask if (a&mask) <= 2**11 - 1 else -(2**12) + (a & mask)