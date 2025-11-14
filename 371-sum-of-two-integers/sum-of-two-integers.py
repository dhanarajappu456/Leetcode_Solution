class Solution:
    def getSum(self, a: int, b: int) -> int: 
        mask = (2**32) - 1 
        while(b & mask):
            temp = a^b
            carry = (a&b)<<1
            a = temp
            b = carry
        return a & mask if (a&mask) <= 2**31 - 1 else -(2**32) + (a & mask)