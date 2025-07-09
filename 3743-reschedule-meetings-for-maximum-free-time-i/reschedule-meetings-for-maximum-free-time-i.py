class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        # find the  contiguous time and append to the list 
        # then iterate on the list  in a sliding window fashion , which is of  K+1 LENGTH
    
        gaps  = []
        ans = 0
        s = 0 
        n = len(startTime)
        for i in range(n):
            curr_start_time  = startTime[i]
            prev_end_time  = 0 if i==0 else endTime[i-1]
        
            gaps.append(curr_start_time-prev_end_time)
        
        # there will be test case like
        '''0--17   ,   14---19  and k =1  and eventTime = 34 ,
        in that case we will have gap after the end time of  the last
        interval and the given  eventTime , which also we will  have to consider 
        as the  gap'''


        gaps.append(eventTime-endTime[n-1])
        m  = len(gaps)

        i,j = 0 , 0
        while(j<m):
            s += gaps[j]
            ans  = max(ans, s )
            if j-i+1 <  k+1:
                j+=1
            else:
                s-=gaps[i]
                i+=1
                j+=1 
        return ans