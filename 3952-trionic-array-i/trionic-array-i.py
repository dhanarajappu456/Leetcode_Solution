class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        #cnt keeps track if there is incr or dec portion for each 3 of the compartment 
        cnt  = 0 
        #if length is < 4 then we can have 3 parition 
        if len(nums) <4:
            return False
        n = len(nums)
        i = 1
        #check inc 

        while(i<n and nums[i-1]<nums[i]):
            cnt+=1
            i+=1 
        if  cnt==0 or i>=n:
            return False
       
        cnt =0 
        
        while(i<n and nums[i-1]>nums[i]):
            cnt+=1
            i+=1
        if cnt  == 0 or i>=n:
            return False
       
        cnt  = 0 
        while(i<n and nums[i-1]<nums[i]):
            cnt+=1
            i+=1
        

        return (cnt >=1 and  i>=n)
        
        


        #cheeck dec

        #check in 
        