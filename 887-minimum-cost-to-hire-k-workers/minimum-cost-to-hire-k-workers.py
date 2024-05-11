import heapq as h 
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ratio = [0 for i in range(n)]
        min_heap_quality = []
        #stores the sum k-1 least wage
        min_sum_k=0
        for i in range(n):
            q = quality[i]
            ratio[i] =( wage[i]  / quality[i],quality[i])
        ratio.sort()
        ans = float("inf")
        for i in range(n):
            curr_ratio = ratio[i][0]
            curr_qual = ratio[i][1]
            if len(min_heap_quality)>k-1:
                max_qual  = h.heappop(min_heap_quality)
                max_qual*=-1
                min_sum_k-=max_qual
            if len(min_heap_quality)==k-1:
                ans  = min(ans, ratio[i][0]*min_sum_k + curr_ratio*curr_qual)
            h.heappush(min_heap_quality,-curr_qual)
            min_sum_k += curr_qual
        return ans 


        

        