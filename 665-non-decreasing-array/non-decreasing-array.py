#when there is a conflict , 
'''
it is always better to make the
nums[i-1] reduced to nums[i], until unless it is not possible 
that is nums[i-2] would conflict , if we change that .
In that case, we increase the nums[i] to nums[i-1]



when we chage we increase the counter , and 
we have already made a change , and need to solve the conflict 
again in another location ,  we return false .

else if we just need to change at max one time the conflict 
then we return true
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        n  = len(nums)
        cnt=0    # counter for number of violations
        
        for i in range(1,len(nums)):
            
            if nums[i-1]>nums[i]:
                if (i-2>=0 ) and (nums[i-2]>nums[i]):
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]

                cnt+=1
            if cnt>=2:
                return False
        return True