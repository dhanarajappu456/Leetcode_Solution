class Solution:
    def minOperations(self, nums: List[int]) -> int:

        #to get only unique elements
        n =len(nums)
        nums = sorted(set(nums))

      
        r=0 
        ans  = n
        for l in range(len(nums)):
            end = nums[l]+n-1
            while(r<len(nums) and nums[r]<=end):
                r+=1
            windowLen  = r-1-l+1
            ans = min(ans,n - windowLen)
        return ans
     
        