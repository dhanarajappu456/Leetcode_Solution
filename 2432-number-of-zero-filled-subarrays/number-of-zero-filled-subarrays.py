class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        prev_non_z = -1
        ans = 0
        for i, num in enumerate(nums):
            if  num ==0:
                ans+=  (i-prev_non_z)

            if num!=0 :
                prev_non_z = i
        return ans