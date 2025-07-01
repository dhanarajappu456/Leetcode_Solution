from collections import defaultdict as dict 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict(int)
        for i,num  in enumerate(nums):
            if (target - num) in mp:
                return [mp[target - num] ,i]
            mp[num] = i
        return [-1,-1]




        