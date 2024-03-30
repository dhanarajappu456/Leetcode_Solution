class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt  = defaultdict(int)
        l1,l2,r = 0,0,0
        ans=0
        while(r<n):
            #adds current char to the window
            cnt[nums[r]]+=1
            #when the number of unique char in the window , 
            #changes to k+1, we need to find the point where it again 
            #become k, by popping th values from left, by shifting(l1)
            while(len(cnt)>k):
                cnt[nums[l2]]-=1
                if cnt[nums[l2]] ==0:
                    cnt.pop(nums[l2])
                
                l2+=1
                #we need to now move the l1 pointer to the new location of l2
        
                l1=l2

            #to find the extreme boundary b.w l1 and l2 
            #when the count of chars at l2 is >1 
            # in the window(l1 to r), then we need to move l2 , until we find the point where no more 
            #we can have a shorter window l2 to r that contain k unique chars
            #eg  = [1,1,1,1,2], k=2
            # here when r  =4 we might need to have l1 at 0 , and l2 at3 
            #as l1 to r is the largest subarray ending at r with k dist chars
            # and l2 to r is shortest window ending at r with k dist chars
            while(cnt[nums[l2]]-1!=0):
                cnt[nums[l2]]-=1
                l2+=1
            if len(cnt)==k:
                ans+= (l2-l1+1)
            r+=1
        return ans
