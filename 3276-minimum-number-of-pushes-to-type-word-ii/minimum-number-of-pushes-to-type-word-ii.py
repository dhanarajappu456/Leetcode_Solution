import heapq as h 

class Solution:
    def minimumPushes(self, word: str) -> int:
        max_heap = []
        letter_cnt   = Counter(word)
        for c in letter_cnt:
            h.heappush(max_heap,(-letter_cnt[c],c))
    
        ans = 0 
        #increased once per each unique character, 
        #which denote position among all unique letters in the word
        position = 0
        while(max_heap):
            occur , c  = h.heappop(max_heap)
            occur *= -1
            #this is the position among the places mapped to a particular character
            #which is nothing  but rounds, the alog first fills first position of all numbers 
            #then second and so on 
            pos = position//8 +1 
            ans  += pos*occur
            position+=1
           
        return ans


            




        
        