class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # deck.sort()
        # n = len(deck)
        # deq = deque([i  for i in range(n )])
        # res= [0 for i in range(n)]
        # for num in  deck:
        #     i = deq.popleft()
        #     res[i] = num
        #     if deq: 
        #         deq.append(deq.popleft())
        # return res 
        n  = len(deck)
        deck.sort()
        res =[-1 for i in range(n)]
        i =0
        for ind , num in enumerate(deck):
            res[i]  = num
            if ind<n-1:
                while(res[i]!=-1):
                    i = (i+1)%n
                i =(i+1)%n
                while(res[i]!=-1):
                    i = (i+1)%n
        return res
        
            

            
            




        