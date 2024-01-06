class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(profit)
        jobs = [(startTime[i],endTime[i], profit[i]) for i in range(n) ]
        jobs.sort()
        def binSearch(i): 
            l = i+1
            h = n-1

            #finding nearest right neibhgbour that is non ovelapping
            ans  = n 
            while(l<=h):
                m =(l+h)//2
                if jobs[m][0]>=jobs[i][1]:
                    ans  = m
                    h = m-1
                else:
                    l = m+1
            return ans
        @lru_cache(None)
        def rec(i):
            
            if i ==n:
                return 0

            ind = binSearch(i)
            
            tk = jobs[i][2] + rec(ind)
            not_ =  rec(i+1 )

            return max(tk,not_)
        
        return rec(0)



            
