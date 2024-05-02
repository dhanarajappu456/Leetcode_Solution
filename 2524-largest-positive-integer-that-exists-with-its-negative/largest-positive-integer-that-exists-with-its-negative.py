class Solution:
    def findMaxK(self, nums: List[int]) -> int:


        nums = set( nums)
        max_ = -1
        for num in nums:
            if( -num in nums) and max_<num:
                max_ = num
        return max_
        