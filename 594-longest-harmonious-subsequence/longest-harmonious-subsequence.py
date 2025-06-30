from collections import defaultdict as dict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        mp = dict(int)
        ans = 0
        for i,num in enumerate(nums):
            if num not in mp:
                mp[num] = i
            if num-1 in mp:
                ans = max( ans , i -mp[num-1] + 1 )
        return ans

    
            

        