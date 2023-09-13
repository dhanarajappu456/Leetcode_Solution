class Solution:
    def candy(self, ratings: List[int]) -> int:
        

    
        '''
        the idea is  we have to go on giving 1 extra cand y as we find the increasing slope  , 
        if we find decreasing slope , then we must star incremneting the canding starting from the dip of it(it is same 
        as incermenting the candy as we go down the decreasing slope)
        '''
        
        n =len(ratings)
        i=1
        cand = n #1 candy should be alwways given

        while(i<n): 
            
            #if it is plateau, then just continue , as already 1 candy has been added to the calulation 

            if ratings[i-1] ==ratings[i]:
                i+=1
                continue
            #increasing slope
            peak=0
            while(i<n and ratings[i-1]<ratings[i]):
                peak+=1
                cand += peak
                i+=1 

                if i ==n:
                    return cand
            #decreasing slope
            dip   = 0
            
            while(i<n and ratings[i-1]>ratings[i]):
                dip+=1
                cand += dip
                i+=1 

            #the peak candy is always the max among left and right neib, so remove the min candy at the peak alreasy #added to the candy
            cand = cand - min(peak,dip)
        return cand
            
            
