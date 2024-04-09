class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:


        # front,back  =Counter( tickets[:k]), Counter(tikets[k+1:])
        # needed = tickets[k]
        # ans = 0 
        # while(needed):

        #     ans += len(front),len(back)
        #     for k in front:
        #         front[k]-=1
        #         if front[k] ==0:
        #             front.pop(k)

        #     for k in back:
        #         back[k]-=1
        #         if back[k] ==0:
        #             back.pop(k)
        #     needed-=1
        # return ans
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
        