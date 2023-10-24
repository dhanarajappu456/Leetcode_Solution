
'''

like the tabulation we use in the lis , dp  store at each index ind,  what is the max constrained sum wnding at nums[ind]

the inner loop of  earlier tabulation is optimised with sliding window max

'''
import heapq as h 
class Solution:
    def constrainedSubsetSum(self, nums, k):
        maxHeap = [ ]
        h.heapify(maxHeap)
        n =len(nums)
        dp = [ nums[i] for i in range(n)]
        for i in range(n):
            #this part is essentially findin the max dp[j] in the sliding window of size k from i-1 , i-2  ....i-k 
            while(maxHeap and i-maxHeap[0][1]>k):
                h.heappop(maxHeap)
            if maxHeap :
            
                dp[i] = max(dp[i], nums[i] +  -maxHeap[0][0])
            h.heappush(maxHeap,(-dp[i],i))    
        return max(dp) 


        '''

        t : n*lok
        s  n
        '''



        