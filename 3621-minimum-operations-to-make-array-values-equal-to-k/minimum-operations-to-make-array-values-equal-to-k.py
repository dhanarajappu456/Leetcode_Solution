import heapq as h 
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt  = 0
        for num in set(nums):
            if num<k:
                return -1
            elif num >k :
                cnt+=1
        return cnt
        


        