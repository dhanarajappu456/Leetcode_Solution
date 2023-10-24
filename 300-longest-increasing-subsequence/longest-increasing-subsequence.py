class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n= len(nums)
        
      
        next_ = [0 for j in range(n+1)] 
        
        for ind in range(n-1, -1,-1):
            temp =  [0 for j in range(n+1)] 
            for preInd in range(-1,ind):
                take= float("-inf")
                if preInd==-1 or nums[ind]>nums[preInd]:
                    take   = 1+ next_[ind+1]
                notTake = next_[preInd+1]
                temp[preInd+1] =  max(take,notTake)
            next_ =temp
        return next_[0]

