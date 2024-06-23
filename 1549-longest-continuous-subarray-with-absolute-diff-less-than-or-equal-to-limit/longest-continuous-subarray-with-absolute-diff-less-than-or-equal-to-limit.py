import heapq as h

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:  
        #identifies  the min and max of the current subarray
        min_heap,max_heap=[],[]
        n = len(nums)
        #note , i is at -1 initally as i is index value upto which element is need to be removed
        ##including the ith value 
        #so length is j-i , we need i to be -1, to deal with edge case , where entire array can be a 
        #valid ans 
        #eg: [2,5,2] ,limit =9 
        #
        i,j =-1, 0 
        ans = 0

        while(j<n):
            h.heappush(min_heap, (nums[j],j))
            h.heappush(max_heap, (-nums[j],j))
    
            #the diff b/w min and max in the subarray need to be<limit
            #else pop the max or min element (whichever comes first in the array) 
            #that cause the diff to be>limit
        
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





        