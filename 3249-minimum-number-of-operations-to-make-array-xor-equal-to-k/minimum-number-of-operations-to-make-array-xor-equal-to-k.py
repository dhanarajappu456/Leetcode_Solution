'''
solution 1 - bit manipulation
the idea is take xor of all elements in the array and check which all position in k and this xor value differ 
in which case we need to flip that position.

t  n

s  1 
'''

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0 
        for num in nums:
            xor ^= num
        res = 0
        cnt=0
        while(cnt!=32):
            
            if (xor & 1) != (k &1): 
                res+=1
            xor >>= 1 
            k >>= 1
            cnt+=1
        return res


        