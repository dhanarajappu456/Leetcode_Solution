import heapq as h

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap =  []
        h.heapify(min_heap)
        for (i,num) in enumerate(nums):
            h.heappush(min_heap, (num,i))
            if len(min_heap)>k:
                h.heappop(min_heap)
        ans  = [ ]
        min_heap.sort(key = lambda x: x[1])
        for (num,i) in (min_heap):
            ans.append(num)
        return ans
        