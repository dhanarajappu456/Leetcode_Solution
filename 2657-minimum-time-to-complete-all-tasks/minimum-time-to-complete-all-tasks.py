class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        tasks.sort(key = lambda x:x[1]) 
        global_set =set() 
        for inter in tasks:

            s,e,d = inter

            taken_curr = set() 
            rem = d 
            for j in range(s,e+1):
                if j in  global_set:
                    taken_curr.add(j)

                    rem-=1 

                if rem==0:
                    break
            j = e 
            while(j>=s and rem):
                if j not in taken_curr:
                    taken_curr.add(j)
                    global_set.add(j)
                    rem-=1
                j-=1 
           
        return len(global_set)

        