class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:


        #solution 2 - 
        #without queue 
        # t n
        #s 1
        ans = 0 
        for i,num in enumerate(tickets):
            #values to left of k
            if i<=k:

                ans += min(num ,  tickets[k])
            #values to right of k 
            else:
                ans += min(num, tickets[k]-1)
        return ans 