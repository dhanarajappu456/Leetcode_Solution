import heapq as h 

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        h.heapify(min_heap)
        n =len(arr)
        for i in range(n-1):
            for j in range(i+1,n):

                fr = arr[i]/arr[j]
             
                if len(min_heap)<k:
                    h.heappush(min_heap, (-fr,arr[i],arr[j]))
                elif fr<-min_heap[0][0]:
                    h.heappop(min_heap)
                    h.heappush(min_heap, (-fr,arr[i],arr[j]))
            
      
        return [min_heap[0][1],min_heap[0][2]]

