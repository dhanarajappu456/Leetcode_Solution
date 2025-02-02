class Solution:
    def check(self, nums: List[int]) -> bool:
        rot_point = None
        i = 0
        n = len(nums)
        while(i<n):
            if (nums[(i-1)%n]>nums[i]<=nums[(i+1)%n]):
                rot_point =i
                break
            if (nums[(i-1)%n]>=nums[i]<=nums[(i+1)%n]):
                rot_point =i
            
            i+=1
        if rot_point == None:
            return False
        cnt = 0
        j = rot_point
  
        while(j!=None and cnt!=n):
        
            if (j!=rot_point) and (nums[(j-1)%n]>nums[j]):
               
                return False
                
            if (cnt!=n-1) and (nums[(j+1)%n]<nums[j]):
               
                return False
            j = (j+1)%n
            cnt+=1
        return True