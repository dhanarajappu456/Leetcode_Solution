class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i=0
        j=0
        n = len(nums)
        ans = 0
        if n ==1:
            return nums[0]
        while(i<n):
            i= j
            s = 0
            while(j<n  and (i==j or nums[j-1]<nums[j])):
                s += nums[j]
                j+=1
            ans =  max(ans , s)
        return ans

            