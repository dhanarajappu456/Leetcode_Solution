import heapq as h 
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap  = nums
        h.heapify(min_heap)
        op =  0 
        while(min_heap and min_heap[0]<k):
            x, y = h.heappop(min_heap) , h.heappop(min_heap)
            h.heappush(min_heap, min(x,y)*2 + max(x,y))
            op+=1
        return op

    