class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
       
        nums = [ (num, i  ) for (i,num) in enumerate(nums)]
        nums.sort()
        i,j    =  0,n-1
        while(i<j):

            if nums[i][0] + nums[j][0]> target:
                j-=1
            elif nums[i][0] + nums[j][0] <  target:
                i+=1
            else:
                return [nums[i][1] , nums[j][1]]
    
                
            
        