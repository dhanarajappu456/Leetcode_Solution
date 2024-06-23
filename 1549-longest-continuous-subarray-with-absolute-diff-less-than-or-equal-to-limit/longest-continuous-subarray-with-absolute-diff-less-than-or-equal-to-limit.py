import heapq as h

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:  
        #identifies  the min and max of the current subarray
        min_heap,max_heap=[],[]
        n = len(nums)
        i,j =-1, 0 
        ans = 0

        while(j<n):
            h.heappush(min_heap, (nums[j],j))
            h.heappush(max_heap, (-nums[j],j))
    
            #the diff b/w min and max in the subarray need to be<limit
            while(min_heap and max_heap and ((-max_heap[0][0] - min_heap[0][0])>limit)):
                
                if min_heap[0][1] <= max_heap[0][1] :

                    i = min_heap[0][1]
                else: 
                    i = max_heap[0][1]

                while(min_heap[0][1]<=i):
                    h.heappop(min_heap)
                
                while(max_heap[0][1]<=i):
                    h.heappop(max_heap)
            
            ans  = max(j-i, ans )
            j+=1 
        return ans 



        