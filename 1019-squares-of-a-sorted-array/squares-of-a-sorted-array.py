class Solution:
    def sortedSquares(self, nums):
        arr=[0 for i in range(len(nums))]
        left=0
        right=len(nums)-1
        curr=len(nums)-1
        while(left<=right):
            if(nums[left]**2>=nums[right]**2):
                
                arr[curr]=nums[left]**2
                left+=1
                curr-=1
            elif(nums[left]**2<nums[right]**2):
                
                arr[curr]=nums[right]**2
                right-=1
                curr-=1
        return arr  