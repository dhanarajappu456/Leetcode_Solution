import heapq as h 
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        split_adj_sum_mx_heap = []
        split_adj_sum_mn_heap = []
        n = len(weights)
      
        #create the max and min heap , 
        # where each element is sum of element on
        #either sides of the split made
        for i in range(1,n):
            sm = weights[i]+ weights[i-1]
            h.heappush(split_adj_sum_mx_heap , -sm)
            h.heappush(split_adj_sum_mn_heap , sm)
      
        min_ = weights[0] + weights[-1]
        max_ = weights[0]  + weights[-1]
        rem_splits  = k-1
        while(rem_splits):
            max_ += -h.heappop(split_adj_sum_mx_heap)
            min_ +=  heappop(split_adj_sum_mn_heap)
            rem_splits-=1
        return max_ - min_





        


