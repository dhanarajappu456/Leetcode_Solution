class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        lowerNums = set()
        nums.sort()
        ans  =0 
        for num in nums:
            if num in lowerNums:
                ans+= (len(lowerNums)-1)
            else:
                ans+= len(lowerNums)
            lowerNums.add( num)
        return ans  
        