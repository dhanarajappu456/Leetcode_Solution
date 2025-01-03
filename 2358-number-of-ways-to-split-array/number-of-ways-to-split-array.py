class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        sm =0 
        tot = sum(nums)
        cnt  =  0 
        n = len(nums)
        for i, num in enumerate(nums):
            sm+= num
            if i<n-1:
                if sm>= (tot-sm):
                    cnt+=1
        return cnt