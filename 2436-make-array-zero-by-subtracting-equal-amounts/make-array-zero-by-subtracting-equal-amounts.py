import heapq as h 
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0 
        unique_ele= set(nums)
        unique_ln = len(unique_ele)
        
        if 0 in unique_ele:
            return unique_ln -1
        return unique_ln
