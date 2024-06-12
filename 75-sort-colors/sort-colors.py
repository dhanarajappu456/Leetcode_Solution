class Solution:
    def sortColors(self, nums: List[int]) -> None:    
        n = len(nums)
        low,i,high = 0,0,n-1
    
        while(i<=high):

            if nums[i]==0:
                nums[low],nums[i] = nums[i],nums[low]
                low+=1
            if nums[i]==2:
                nums[high],nums[i] = nums[i],nums[high]
                high-=1
                #edge case 
                # nums =
                # [1,2,0]

                # Use Testcase
                # Output
                # [1,0,2]
                i-=1
            
            i+=1
           
        return nums


    
        