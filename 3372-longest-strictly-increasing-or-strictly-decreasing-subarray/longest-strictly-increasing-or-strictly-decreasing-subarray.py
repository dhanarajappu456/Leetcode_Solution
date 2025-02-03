class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        equality = 0
        cnt = 0
        ans = 1
        n = len(nums)
        for i in range(n):
            if (nums[i] -  prev) == 0:
    
                equality = 0
            elif (nums[i] -prev)>0:
                if equality==1:
                    cnt+=1
                else:

                    equality =1
                    cnt =2
            elif (nums[i] -prev)<0 :
                if equality==-1:
                    cnt+=1
                else:
                    equality =-1
                    cnt =2
            
            ans = max(ans,cnt)
            prev = nums[i]
        return ans