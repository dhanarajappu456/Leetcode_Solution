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
        while(max_heap):
            mapped_letter_length , num = h.heappop(min_heap)
            occur , c  = h.heappop(max_heap)
            occur *= -1
            pos = mapped_letter_length+1
            ans  += pos*occur
            h.heappush(min_heap, (pos,num))
        return ans


            




        
        