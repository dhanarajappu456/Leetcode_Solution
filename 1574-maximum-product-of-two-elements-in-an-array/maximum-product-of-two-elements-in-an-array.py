'''
#solution 1 - sorting , finding the first and second max which is at first and second last place 
t nlogn
s 1

#solution 2 - with no sorting 
finding the first and second last element in the array 

t n 
s 1


'''

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



