class Solution(object):
    def maxSubarrays(self, nums):
        
        '''

        the crux of the solution lies, in the property of AND

        when we and a couple of numbers one by one , the result is either same as previous result or less than that
        thus it is always favourable to include all numbers in the sams single array to get the minimum , 

        until and unless when there are 0  or result of the subarray is 0 ,

        when there are zero anding with all the non zero numbres gives 0 as the answer which is the minimum score, 
        now, essentially we need to split the array , at indices, where we get zero as the answer of anding 
        '''

        curr = (1<<32)-1
        cnt  = 0 
        for num in nums:
            curr  = curr & num
            if curr == 0:
                cnt+=1
                curr = (1<<32)-1
        
        return max(1,cnt) 

            
        