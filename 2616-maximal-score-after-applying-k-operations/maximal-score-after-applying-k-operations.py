import heapq as h
import math as m 
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n  = len(nums)
        for i in range(n):
            nums[i]  = -nums[i]
        h.heapify(nums)

        res = 0
        while(k):
            num  =  -h.heappop(nums)
            res+= num
            num = m.ceil(num/3)
            h.heappush(nums, ( -num ))
            k-=1
        
        return res