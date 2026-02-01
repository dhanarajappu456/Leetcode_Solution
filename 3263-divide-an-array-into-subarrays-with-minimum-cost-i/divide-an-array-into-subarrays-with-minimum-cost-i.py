class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        arr = sorted(nums[1:])
        return nums[0]  + arr[0] + arr[1] 




