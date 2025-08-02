from collections import defaultdict as dict
import heapq as h
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = dict(int)
        for t in tasks:
            mp[t]+=1
        #max_heap 
        chosable  = []  
        wait_task =deque([])  
        for t in mp:
            h.heappush(chosable , (-mp[t],t))
        ans  = 0 
        t = 0 
        #nlogn
        while(chosable or wait_task):
            #check if any wait task can be added to chosen
            while(wait_task and wait_task[0][0]<=t):
                time1 , count1,  task1 = wait_task.popleft()
                h.heappush(chosable,(-count1, task1))
            if chosable:
                cnt , task = h.heappop(chosable)
                cnt *= -1
                cnt -=1
                if cnt != 0 :
                    wait_task.append((t+n+1, cnt, task))
                    # h.heappush(wait_task, (t+n+1, cnt, task))
            t+=1
        return t





        
        
        



        