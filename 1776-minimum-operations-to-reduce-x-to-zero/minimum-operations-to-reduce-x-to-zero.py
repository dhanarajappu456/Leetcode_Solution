
from collections import defaultdict as dict
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        
        n  = len(nums)
        
        #edge case
        #if complete array sum is ==x , then we need minimum n operations to reduce x to zero
        if sum(nums) ==x:
            return n 
        
        #subarray that sum to k , is neede to be removed
        k =sum(nums) - x
        
        prefixSum = 0
        prefixSumHash =dict(int)
        prefixSumHash[0]=-1
        operations = float("inf")
        
        
        for i,num in enumerate(nums):
             
            prefixSum+=nums[i]
            #checks if subbary of sum k , can be obtained 
            if prefixSum - k in prefixSumHash:
                
                j = prefixSumHash[prefixSum - k]
                length = i-j
                #if the subaarray of sum k of length long , and is removed ,remaining  
                #arraay elements ,sum to x , which is  n  - length long
            
                operations = min(operations, n - length)
            
            prefixSumHash[prefixSum] =i
                   
        return -1 if operations == float("inf") else operations 
            