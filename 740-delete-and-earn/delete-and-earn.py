from collections import defaultdict as dict 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = dict(int)
        nums.sort()
        for i,num in enumerate(nums):

              d[num] = i
  
        n  = len(nums)
  
        @lru_cache(None)
        def rec(ind):


            if ind ==n:
                return 0

           
            next_ind  = d[nums[ind]]+1 if nums[ind]+1 not in d else  d[nums[ind]+1]+1
           
            tk  = (nums[ind] *(d[nums[ind]]-ind+1) )  + rec(next_ind )

            not_  =rec(d[nums[ind]]+1)

            return max(not_, tk)
        return rec(0 )





        