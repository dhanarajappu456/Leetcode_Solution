import heapq as h
from typing import List
#solution 1 

##since we can only increase the number, standing at current number , look for far ther index j till which we can 
#go such that we can increase all the numbers in the rand j to i to make to nums[i], standing with in bound of k 


#solution 2 -optimised , biin search 
#same as the prev approach  , but binary search for the index 

'''for this ,  make an array  k_needed, ith index of  which stores the k value needed  to make a number from 0 to i 
now binary search standing at each index ,with help of this array
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:


        # nums.sort()
        # ans = 1 
            
        # n = len(nums)
        # for i in range(n):
            
     
        #     k_rem =k
        #     j = i
        #     while(j>=0 and nums[i]-nums[j]<=k_rem):
        #         k_rem -= (nums[i]-nums[j])
        #         j-=1
          
        #     ans = max(ans, i-j)
        # return ans

        
        n  = len(nums)
        nums.sort()
        k_needed = [0 for i in range(n)]
      
     
        for i in range(1,n):
            k_needed[i] = k_needed[i-1]+(i)*(nums[i]-nums[i-1])

        def binSearch(i,j):
            index_of_number_to_make = j
            ans =j
            while(i<=j):
                mid = (i+j)//2
                if (k_needed[index_of_number_to_make]-k_needed[mid]-( (mid)*(nums[index_of_number_to_make]-nums[mid]) )  )<=k:
                    
                    ans  = mid
                    j = mid-1
                  
                else:
                    i = mid+1
            return ans
       
        ans = 1 
        for i in range(n):

            ind = binSearch(0,i)
         
            ans = max(ans, i-ind+1)
        return ans 








        