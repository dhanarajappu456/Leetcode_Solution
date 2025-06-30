from collections import defaultdict as dict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = dict(int)
        ans = 0
        for i,num in enumerate(nums):
            count[num]+=1
        for num in nums:
            min_ = num 
            max_ = num+1
            if count[num+1]:
                ans = max(ans , count[num] + count[num+1])
        return ans

    
            

        