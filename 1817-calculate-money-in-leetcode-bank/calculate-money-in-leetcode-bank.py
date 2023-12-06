class Solution:
    def totalMoney(self, n: int) -> int:
        week = 1
        ans =0 
        d = 1
        start =1 
        while(n):
            
            if n>=7:
                


                for i in range(start, start+7):
                    ans+=i
                start+=1
                n = n-7
          
     
            if n<7:
              
                for i in range(start, start+n):
                    ans+= i

            
                n = 0
           
        return ans