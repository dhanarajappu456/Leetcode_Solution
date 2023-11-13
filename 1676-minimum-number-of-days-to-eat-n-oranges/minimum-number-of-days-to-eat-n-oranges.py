from collections import deque as deq


class Solution:
    def minDays(self, n: int) -> int:
    

        q = deq([(n,0)])
        vis  = set()
        while(q):
            #print(q)
            num,days = q.popleft()
            if num-1 ==0:
                return days+1
            if num-1 not in vis:
                q.append((num-1,days+1))
                vis.add(num-1)        
            if num%2 ==0 :
                q.append((num/2,days+1))
                vis.add(num/2)
            if num%3 ==0:
                q.append((num/3, days+ 1))
                vis.add(num/3)

        return -1

        

