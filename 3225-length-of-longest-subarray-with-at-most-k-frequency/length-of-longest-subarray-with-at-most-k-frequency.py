from collections import defaultdict as dict 
#slidinng widow - 
#T n 
#s n - dict 
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt  = dict(int)
        j = 0
        i=0
        ans = 0 
        while(j<n):
            num  = nums[j]
            cnt[num]+=1
            while(cnt[num]>k):
                cnt[nums[i]]-=1
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans 
        