import heapq as h 
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod  = 10**9+7 
        min_heap  = [ ]

        for i, num in enumerate(nums):
            h.heappush(min_heap , (num,i) )
        
        ans = 0 
        index = 1
        while min_heap :
            sm , i  = h.heappop(min_heap)
            if left<=index<=right:
                ans = (ans%mod + sm%mod )%mod
            if i+1<n:
                h.heappush(min_heap, ( sm + nums[i+1],i+1))
            index+=1
            #optimisation - early break out 
            if index>right:
                break
            
        return ans 
                
             

                






        

        