
'''
like subarray with sum == k 

here the sum is number of odd numbers in a subarray
pref stores the sum of odd numbers so far 
'''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        pref,ans   =0 ,0 
        d[0]=1 
        n   = len(nums)
        for i,num in enumerate(nums):
            if num%2 ==1 :
                pref+=1 
            if pref-k in d: 
                ans  += d[ pref-k]
            
            d[pref] +=1 
        return ans 

                
            
            
            
            
            
            