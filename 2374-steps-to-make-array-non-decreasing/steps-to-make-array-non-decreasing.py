'''
solution  using mon increasing stack 
if the value is < top of stack keep on delteting assuming in each step 
at end take max value of step 
t n 
s n 


'''

class Solution:
    def totalSteps(self, nums: List[int]) -> int:

       
        n = len(nums)
        stk = []
        ans =0 
        for num in nums[::-1]:
           
            max_step =0 
            while(stk and num>stk[-1][0]):
                val,steps = stk.pop(-1)
                max_step = max(max_step+1,steps)
            stk.append((num,max_step))
          
            ans  = max(ans,max_step)
        return ans

        