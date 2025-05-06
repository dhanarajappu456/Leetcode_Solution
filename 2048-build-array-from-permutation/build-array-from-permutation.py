class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        


        ans  =  nums[::-1]
        n = len(nums)
        for i in range(n):
            ans[i]  = nums[nums[i]]
        return ans