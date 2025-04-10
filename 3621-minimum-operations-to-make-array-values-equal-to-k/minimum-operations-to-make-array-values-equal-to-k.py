import heapq as h 
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        for num in nums:
            if num < k:
                return -1
        
        cnt  = 0
        arr = list(-num for num in set(nums))
        # for num in arr: 
        #     h.heappush(arr , -num)
        h.heapify(arr)
        print(arr)
        while(arr and  -arr[0]!=k):
            cnt+=1
            h.heappop(arr)
        return cnt


        
        


        