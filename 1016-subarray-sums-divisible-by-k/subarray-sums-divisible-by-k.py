from collections import defaultdict as dict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderCounts = dict(int)
        remainderCounts[0]=1
        n  = len(nums)
        ans= 0
        prefixSum=0
        #we caluclate the number of subarray ending at i whose sum of elements is k
        for i,num in enumerate(nums):
            
            prefixSum += num
            
            #find remainder of totaal prefisum till index i
            remainder = (prefixSum)%k
            
            
            #we check if there are subarray from 0th index, whose sum %p gives the remainder obtained  above
            #means we can remove that portion to get the subarray [someindex+1:i] , which is divisble by p
            
            #note:
            #remeber  remainderCounts[rem] increases by 1 
            #if we find  prefixSum that sum to  rem, rem+k, rem+2k, rem +3k etc....

            
            
            

            if remainder in remainderCounts:
                ans+= remainderCounts[remainder]
            remainderCounts[remainder]+=1
            
        return ans
            
            
            
            
            
        
        