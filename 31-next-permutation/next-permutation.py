class Solution:
    def swap(self, nums,i,j):
        if len(nums)>1:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
    def reverse(self,nums,i):
        s = i
        e = len(nums)-1
        while(s<e):
            temp=nums[s]
            nums[s]=nums[e]
            nums[e]=temp
            s+=1
            e-=1
    def nextPermutation(self, nums):
        i=len(nums)-2
        while(i>-1):
            if(nums[i]<nums[i+1]): 
                break  
            i-=1
        j=len(nums)-1
        while(i!=-1 and j!=i):
            if(nums[j]>nums[i]):
                break
            j-=1
        self.swap(nums,i,j)  
        self.reverse(nums,i+1)  
