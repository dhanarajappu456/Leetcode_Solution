'''#SOLUTION1 
USING DICT AND ARR, WITH SORTING


SOLUTION 2 

USING DICT, MAXHEAP

T N 
S  NLOGN

'''
import heapq as h 
class Solution:
    def frequencySort(self, s: str) -> str:
        d =dict()
        heap =[]
        for c in s:
            d[c]= d.get(c,0)+1
        ans  = []

        for c in d:
            cnt = d[c]
            h.heappush(heap,(-cnt,c))
        while heap:
            cnt,char  = h.heappop(heap)
            ans.append(char*(-cnt))
        
        return "".join(ans)

