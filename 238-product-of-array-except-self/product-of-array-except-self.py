class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        output =[1 for i in range(len(nums))]
        pre_start,suff_start=1,1
        while(i<len(nums)):
            output[i]*=pre_start
            output[j]*=suff_start
            pre_start*=nums[i]
            suff_start*=nums[j]
            i+=1
            j-=1
        return output
            
