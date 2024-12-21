class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        n  = len(nums)
        cnt=0    # counter for number of violations
        
        for i in range(1,len(nums)):
            
            if nums[i-1]>nums[i]:
                if (i-2>=0 ) and (nums[i-2]>nums[i]):
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]

                cnt+=1
            if cnt>=2:
                return False
        return True