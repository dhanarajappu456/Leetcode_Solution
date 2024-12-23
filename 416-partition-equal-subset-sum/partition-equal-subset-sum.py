

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        tar =sum(nums)//2
        prev = [False if i!=nums[0] else True for i in range(tar+1)]
        
        n =len(nums)
      
       #prev[0] = true

        
        for i in range(1,n):

            curr =[False for  j in range(tar+1)]
            for j in range(1,tar+1):
                tk_ = False
                if j> nums[i]:
                    tk_ = prev[j -nums[i]]
                elif tar == nums[i]:
                    tk_ = True 
                not_ = prev[j]

                curr[j] = tk_ or not_
            
            prev = curr 
            
        return prev[tar]











        