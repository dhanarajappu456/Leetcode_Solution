class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        i = 0
        j = 0
        cnt = 0 
        while(i<n):
           
            while(j<n and ((nums[j]-nums[i])<=k)):
                j+=1
            cnt+=1
            i = j
        return cnt 

        