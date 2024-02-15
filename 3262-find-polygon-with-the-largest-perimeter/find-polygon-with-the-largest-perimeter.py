'''
solution pref sum + greedy


the idea is we sort the  nums array 
and we create pref array for this nums

pref[i]which denote sum of all sides from o to i 

next we iterate on nums from end , checking if nums[i] can be the longest 
in which case pref sum till i-1 should be> nums[i]

t n 

s n 
'''
#python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pref = [0 for i in range(n )]
        
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1]+ nums[i]
        ans = -1
        j = n-2
        for i in range(n-1,1,-1):
            
            longest = nums[i]
  

            if pref[i-1]>longest:
                return pref[i-1]+ longest 
        return ans
            