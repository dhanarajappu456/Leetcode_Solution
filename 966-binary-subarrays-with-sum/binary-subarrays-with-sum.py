class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_sum_count =defaultdict(int)
        pref_sum_count[0]=1
        n = len(nums)
        ans = 0
        pref_sum=0 
        for i in range(n):
            pref_sum+=nums[i]
            ans+= pref_sum_count[pref_sum - goal]
            pref_sum_count[pref_sum]+=1
        return ans 
