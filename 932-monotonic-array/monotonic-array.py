class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n =len(nums)
        if nums[0] <= nums[-1]:

            for i in range(1,n):
                if nums[i]>=nums[i-1]:
                    continue
                return False

            return True
        
        

        else:

            for i in range(1,n):
                if nums[i]<=nums[i-1]:
                    continue
                return False
            return True
        