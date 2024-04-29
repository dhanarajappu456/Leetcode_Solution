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


        