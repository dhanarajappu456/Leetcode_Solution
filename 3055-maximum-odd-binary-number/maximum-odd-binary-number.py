class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        
        
        ones = s.count("1")
        
        
        ans =  ["0"  for i in range(len(s))]
        if ones==0:
            return "".join(ans)
        
        ones -=1
       
        ans[-1] = "1"
      
        n= len(s)
        i=0
        while(ones>0 and i<n):
       
            ans[i] ="1"
            ones-=1
            i+=1 
        return "".join(ans)
    
        