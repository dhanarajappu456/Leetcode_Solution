'''
using prev small and next small for  middle element (jth) in i,j,k 

'''

class Solution(object):
    def find132pattern(self, nums):

        n =len(nums)
        stk =[(float("inf"),float("inf"))]
        for i in range(n):
            min_ = float("inf")
            while(stk and stk[-1][1]<=nums[i]):

                minimum , num  = stk.pop(-1)
                min_ = min(min_,minimum)
            if stk[-1][0]< nums[i] and stk[-1][1]>nums[i]:
                return True
            stk.append( (min(min_, stk[-1][1],nums[i ]) , nums[i]))
       
        return False