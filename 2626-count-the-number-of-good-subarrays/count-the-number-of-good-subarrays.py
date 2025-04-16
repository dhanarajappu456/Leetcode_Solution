from collections import defaultdict as dict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        mp  = dict(int)
        ans  = 0 
        n = len(nums)
        j = 0 
        i = 0
        pairs = 0
        while(j<n):
           
            pairs += mp[nums[j]]
            mp[nums[j]]+=1
            while(pairs>=k):
                ans+= n-j
                mp[nums[i]] -=1
                #nums[i] contribute , mp[nums[i]]-1 times
                pairs-= mp[nums[i ]]
                i+=1
            j+=1

        return ans