

'''
Solution 1 - 
like subarray with sum == k 

here the sum is number of odd numbers in a subarray
pref pref sum which is the sum of count of odd numbers so far 

the array can be imagined as :
[1,1,2,1,1]----> [1,1,0,1,1]
t n 
s n 

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

                
            
            
            
            
            
            