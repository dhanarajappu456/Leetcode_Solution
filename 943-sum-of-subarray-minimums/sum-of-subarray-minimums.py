class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nums = arr
        n  = len(nums)
        def prevSmaller():
            prevSmall = [-1 for i in range(n)]
            stk =[(-1,-1)]
            
            for i,num in enumerate(nums):
                
                while(stk and stk[-1][0]> num):
                    
                    stk.pop(-1)
                    
               
                smallNumb,index =stk[-1]
                prevSmall[i] = index
                stk.append((num,i))
                
            return prevSmall
            
        def nextSmaller():
            nextSmall = [-1 for i in range(n)]
            stk =[(-1,n)]
            
            for i,num in reversed(list(enumerate(nums))):
                
                while(stk and stk[-1][0]>= num):
                    
                    stk.pop(-1)
                    
               
                smallNum,index =stk[-1]
                nextSmall[i] = index
                stk.append((num,i))
            return nextSmall
                       

                
        
        prevSmall = prevSmaller()
        nextSmall = nextSmaller()
        
            
        ans= 0 
        mod = 10**9+7
        for i ,num in enumerate(nums):
            totalSubarrays =0
            left=  i-prevSmall[i]
            right = nextSmall[i]-i
            
            totalSubarrays = left*right
            ans  = (ans + ( totalSubarrays*num))%mod
        

        
        return ans
        