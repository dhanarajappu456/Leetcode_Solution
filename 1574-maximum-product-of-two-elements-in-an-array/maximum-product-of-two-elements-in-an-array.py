class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max,second_max = -1, -2 
        n = len(nums)
        for i in range(n):

            if nums[i]>=first_max : 
                second_max = first_max
                first_max = nums[i]
            elif nums[i]>second_max:
              
                second_max = nums[i]
          
        return (first_max -1 )* (second_max-1)



