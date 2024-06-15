#Note the capital not decrease on choosing a project, we only 
#get the capital increased each time 
#so this point to select project with max profit at any time which has a capital requiremnet<=balance we have
#so we use heap here
import heapq as h 

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #minHeap for  getting all the project that we an afforde with current wallet balance
        minHeap = [(c,p) for p,c in zip(profits, capital)]
        h.heapify(minHeap)

        #maxHeap to get the project that yield more profit among all other project that we can afford
        maxHeap = [ ]
        h.heapify(maxHeap)
        balance = w
        while(k):
            while(minHeap and minHeap[0][0]<=balance):
                c,p  = h.heappop(minHeap)
                h.heappush(maxHeap,-p)

            if maxHeap:
                prof= h.heappop(maxHeap)
                balance+= (-prof)
            k-=1
        #return the final balance
        return balance

        
