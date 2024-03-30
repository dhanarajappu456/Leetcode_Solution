class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt  = defaultdict(int)
        l1,l2,r = 0,0,0
        ans=0
        while(r<n):
            print(r)
            cnt[nums[r]]+=1
            while(len(cnt)>k):
                cnt[nums[l2]]-=1
                if cnt[nums[l2]] ==0:
                    cnt.pop(nums[l2])
                l2+=1
                l1=l2
            while(cnt[nums[l2]]-1!=0):
                cnt[nums[l2]]-=1
                l2+=1
            if len(cnt)==k:
                ans+= (l2-l1+1)
            r+=1
        return ans
