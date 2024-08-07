#based on idea remainder keeps repating(when divides by k) , when k or multiple of k 
#is added to a number 
from collections import defaultdict as dict 
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainderToIndex =dict(int)
        remainderToIndex[0]= -1
     
        prefixSum =0
        for i,n in enumerate(nums):
            
            prefixSum+= n
            rem = prefixSum%k
            
            if rem in remainderToIndex:
                #note that we dont updatt the rem  if 
                #it is already there as we need to have smallest index 
                #for a rem , as we are greedy to have length>=2
                length  = i-remainderToIndex[rem]
                if length>=2:
                    return True 
            else:
                
                remainderToIndex[rem]= i
   
        return False