'''
#Solution 1 
sort and choose the 2 top element and 2 small element and find diff
t nlogn
s 1 

'''


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:


        nums.sort()

        return (nums[-1]*nums[-2])- (nums[0]*nums[1])