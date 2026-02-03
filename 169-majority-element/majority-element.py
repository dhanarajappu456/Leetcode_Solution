class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev = nums[0]
        cnt  = 0 
        for num in nums:
            if( cnt == 0) or (prev  == num):
                cnt+=1
                prev  = num 
            else:
                cnt-=1    
        return prev
    
            