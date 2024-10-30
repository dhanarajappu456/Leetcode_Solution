class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans  = set()
        n  = len(nums)
        nums.sort()

        z_set = set()
        for i in range(n-1,0, -1):
           
            for j in range(i-1,-1,-1):
                y,x  = nums[i],nums[j]
                if -(x+y) in z_set:
                    ans.add((x,y,-(x+y)))   
            z_set.add(nums[i])
          
        return list(ans) 



        
        