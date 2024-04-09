class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:


        #simulation 1 
        #t - kn
        #s   n 
        t  =deque([(i,num) for i,num in enumerate(tickets)])
        need = tickets[k]
        ans = 0 
        while(need):
            ind, val  =t.popleft()
            val-=1
            if val!=0:
                t.append((ind, val))
            if ind ==k:
                need-=1
            ans+=1

        return ans
        