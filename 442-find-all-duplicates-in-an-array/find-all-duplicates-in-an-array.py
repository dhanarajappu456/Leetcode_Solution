#using the -ve sign to identify the presence of a number
from collections import defaultdict as dict 


class Solution:
    def findDuplicates(self, nums):
        ans =[]
        for i,n in enumerate(nums):
            n = abs(n)
            index = n-1
            #if n is duplicate , the index nums[n-1] would have 
            #already made to -ve
            if nums[index ] <0 :
                ans.append(n)
            else:
                
                nums[index] = -nums[index]
       
        return ans