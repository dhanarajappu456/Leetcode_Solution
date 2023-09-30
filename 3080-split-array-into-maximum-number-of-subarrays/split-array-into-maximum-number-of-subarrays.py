class Solution(object):
    def maxSubarrays(self, nums):
        


        curr = (1<<32)-1
        cnt  = 0 
        for num in nums:
            curr  = curr & num
            if curr == 0:
                cnt+=1
                curr = (1<<32)-1
            

        return max(1,cnt) 

            
        