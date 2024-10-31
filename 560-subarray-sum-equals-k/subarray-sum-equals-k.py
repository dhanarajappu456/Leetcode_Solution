from collections import defaultdict as dict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        dict_ = dict(int)
        total = 0
        dict_[0]=1
        prefixSum = 0
        target =k
        for n in nums:
            prefixSum +=n
         
            if prefixSum- target in dict_:
                total +=  dict_[prefixSum- target] 
            dict_[prefixSum]+=1
            
        return total