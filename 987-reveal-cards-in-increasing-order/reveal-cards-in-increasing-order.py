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


        