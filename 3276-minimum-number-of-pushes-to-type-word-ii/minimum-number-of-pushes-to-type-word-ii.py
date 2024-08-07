import heapq as h 

class Solution:
    def minimumPushes(self, word: str) -> int:
        max_heap = []
        letter_cnt   = Counter(word)
        for c in letter_cnt:
            h.heappush(max_heap,(-letter_cnt[c],c))
        min_heap  =[ (0,i) for i in range(2,10)]
        h.heapify(min_heap)
        ans = 0 
        mapped  = {}
        position = 0
        while(max_heap):
    
            occur , c  = h.heappop(max_heap)
            occur *= -1
            pos = position//8 +1 
            ans  += pos*occur

            position+=1
           
        return ans


            




        
        