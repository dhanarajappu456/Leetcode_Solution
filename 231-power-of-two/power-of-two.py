class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        

        if n<=0: 
            return False
        
        maxPow2 = 2**30

        return maxPow2%n ==0
        