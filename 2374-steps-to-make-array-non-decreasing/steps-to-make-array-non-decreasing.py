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
           
            cnt =0 
            while(stk and num>stk[-1][0]):
                
                val,steps = stk.pop(-1)
                #when i remove a number right to the num1 lets say num2   ,
                #then it must have stored  number of steps to remove elements ro right of num2 ,
                # then number of steps to remove nums to right of num1 
                #is just == steps if number of step needed to delete numbers to right of num1(cnt+1)< step
                cnt = max(cnt+1,steps)
            stk.append((num,cnt))
          
            ans  = max(ans,cnt)
        return ans

        