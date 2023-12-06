'''
solution1 - simultion

'''

class Solution:
    def totalMoney(self, n: int) -> int:
    
        ans =0 
        start =0
        while(n):
            
            if n>=7:
                end = start+7
   
                ans+= (end*(end+1)//2 - start*(start+1)//2)
                start+=1
                n-=7 

            if n<7:

            
                for i in range(start+1, start+1+n):
                   
                    ans+= i
            
                n = 0
           
        return ans