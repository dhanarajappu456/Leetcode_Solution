
'''

using three pointer , low  high and i 
low keeps track of 0 and high for 2 and i is the current pointer 

the edge case is when we find curren value as 2 and swap it with high , the high would have been
pointing to the 0 , and wehen swapping it might therefore put this 1 after some 0 
to deal with this we dont update the i when current value found is 2 
t n 
s  1 

'''

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

                #when current value found is 2 we dont necessarily update i , 
                #as this the swapped value coming from high would be 0 , which 
                #need to be dealt in next iteration , as this might bring 0 after some 1's 
        
                i-=1
            
            i+=1
           
        return nums


    
        