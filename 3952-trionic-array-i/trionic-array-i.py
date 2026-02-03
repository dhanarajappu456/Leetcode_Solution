class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        cnt  = 0 
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
        print(1,i)
        cnt =0 
        while(i<n and nums[i-1]>nums[i]):
            cnt+=1
            i+=1
        if cnt  == 0 or i>=n:
            return False
        print(2,i)
        cnt  = 0 
        while(i<n and nums[i-1]<nums[i]):
            cnt+=1
            i+=1
        print(3,i)

        return (cnt >=1 and  i>=n)
        
        


        #cheeck dec

        #check in 
        