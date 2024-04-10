#using queue
#solution 2 l
#like the simulation , 
#we place the  the number is in the sorted deck to  index i of res , then skipo next psotion and store
#these skipped index somewhere ,  
#and so on , once we  reach end of res, we need to  place next num in dec to the indices in thesen the skipped indices
#in fifo , that is why we store these indices in queue
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        deq = deque([i  for i in range(n )])
        res= [0 for i in range(n)]
        for num in  deck:
            i = deq.popleft()
            res[i] = num
            if deq: 
                deq.append(deq.popleft())
        return res 

    #t nlogn(sort) + n^2 (overall loop )
    #s 1 
