'''
#Solution 1 
sort and choose the 2 top element and 2 small element and find diff
t nlogn
s 1 



#Solution 2
itearate the array , parallely update max1,max2 , min1 , min2 
t n
s 1 

'''

#solution 2 
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        

        min_1, min_2  = float("inf") , float("inf")

        max_1, max_2  = -1, -1

        n = len(nums)

        for i in range(n):

            if nums[i]<= min_1 :
                min_2  = min_1 
                min_1 =  nums[i]

            elif nums[i]<=min_2:
             
                min_2 =  nums[i]

            if nums[i]>= max_1:
                max_2 = max_1 
                max_1 = nums[i]
            elif nums[i] >= max_2 :
                max_2 = nums[i]
           
        return  (max_1*max_2) - (min_1*min_2)
