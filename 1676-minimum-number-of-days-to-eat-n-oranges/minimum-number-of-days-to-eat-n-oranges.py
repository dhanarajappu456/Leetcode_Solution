from collections import deque as deq

#bfs all 3 choices, 
class Solution:
    def minDays(self, n: int) -> int:
    

        q = deq([(n,0)])
        vis  = set()
        while(q):
          
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

    # t = 3^mindays(3 choices at each level ,) , ans also we dont visit same node again , )
    #     mindays will be log(n,2) at worst , 
    #     then 3^mindays, will still not be that efficient it seems , but in fact it is as we dont visit visited nodes again 
    # s =  3^minDays

        

