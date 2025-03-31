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
        #the values at the extreme ends gonna be end of 
        #some parition , which contribute to the sum
        min_ = weights[0] + weights[-1]
        max_ = weights[0]  + weights[-1]

        #we need to make k-1 splits for the k partition
        rem_splits  = k-1
        while(rem_splits):
            #choose to split at a point where sum 
            #of element on either side of the split is max
            max_ += -h.heappop(split_adj_sum_mx_heap)
            #choose to split at a point where sum of 
            #element on either side of split is  min
            min_ +=  heappop(split_adj_sum_mn_heap)
            rem_splits-=1
        return max_ - min_





        


