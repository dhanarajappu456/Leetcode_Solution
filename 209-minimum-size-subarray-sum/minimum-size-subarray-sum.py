class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        removedPrefixSum = 0
        ans = float("inf")
        n = len(nums)
        sub_sum = 0 
        i,j = 0,0
        while(j<n):

            sub_sum  +=  nums[j]
            if sub_sum  < target:
                j+=1
                continue
            else:
                while(sub_sum>=target):
                    ans  = min(ans, j-i+1)
                    sub_sum-=nums[i]
                    i+=1
                j+=1
        return 0 if ans == float("inf") else  ans


        
        
            