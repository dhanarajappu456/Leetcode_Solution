class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        tasks.sort(key = lambda x:x[1]) 
        taken =set() 
        for inter in tasks:
            s,e,d = inter
            rem = d 
            for j in range(s,e+1):
                if j in  taken:
                    taken.add(j)
                    rem-=1 
                if rem==0:
                    break
            j = e 
            while(j>=s and rem):
                if j not in taken:
                    taken.add(j)
                    rem-=1
                j-=1 
           
        return len( taken)

        