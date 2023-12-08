'''
brute force each rotation , 

each ith rotation cost i*x cost additonaly 

in ith itaration j+ith  element comes int position j , see if it is less than value at j 
in which that is the new value at j  th element comes to 

the mins list keeps the list with min value that can come at each index
'''

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        mins =nums[:]
        ans  = sum(nums)
        n = len(nums)
        for rot in range(n):

            for pos in range(n):


                mins[pos] = min(mins[pos],nums[(pos+rot)%n])

            ans = min(ans, sum(mins)+rot*x)
          
        
        return ans

                
                
                
            
            
            
        
            
            

            
        