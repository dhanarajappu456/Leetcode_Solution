class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt =0 
        for i in range(n-1,-1, -1):

            cnt+=1
            if ((i ==0  )or ( i-1>=0 and   nums[i-1]<cnt))and nums[i]>=cnt:
                return cnt
        
        return -1
        