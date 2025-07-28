class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0

        for num in nums:
            max_or |= num

     
        n = len(nums)
        @lru_cache(None)
        def rec(i,ors):
            
            if i == n : 
                if  ors  == max_or:
                    return 1
                else:
                    return 0
            
            
            return (rec(i+1, ors | nums[i])+  rec(i+1, ors))


        return rec(0,0)
        