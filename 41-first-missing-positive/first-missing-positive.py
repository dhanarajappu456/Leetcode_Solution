class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans  = len(nums)+1

        for i,num in enumerate(nums):
            if num<=0:
                nums[i] = float("inf")
        n = len(nums)
        for i,num in enumerate(nums):
            if abs(num) != float("inf") and (abs(num)-1)<n:
                print(abs(num)-1)
                nums[abs(num)-1] = -abs(nums[abs(num)-1])

        for i in range(n):
            if nums[i]>0:
                return i+1
        return ans
        

        
        
        
        