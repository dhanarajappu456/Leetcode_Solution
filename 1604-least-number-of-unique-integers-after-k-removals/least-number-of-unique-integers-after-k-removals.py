'''
counting and sorting/using min heap


the idea is count occurence of each number 

then sort it and remove the number whose ocuurence is < k reamining


t n + logn
s n 

'''

import heapq as h 

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        d = {}
        heap = []
        for num in arr: 
            
            d[num]  = d.get(num,0)+1
      
        
        for num in d:
            h.heappush(heap,(d[num],num))
        
        
        while(heap and heap[0][0]<=k):

            count, num = h.heappop(heap)
            k-= count
      
        
        return len(heap)