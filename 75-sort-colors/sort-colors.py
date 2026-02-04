class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i,j , k = 0,n-1 , 0


        while(k<n and k<=j):

            if nums[k] ==0:
                nums[i],nums[k] = nums[k], nums[i]
                i+=1
            elif nums[k] ==2:        
                nums[j],nums[k] = nums[k], nums[j]
                #to deal the case wher the elemetn coing from j to k is , 0 
                k-=1
                j-=1
            k+=1

        