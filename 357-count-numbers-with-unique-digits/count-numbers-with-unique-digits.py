class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        
        
  
        res = 0
        for i in range(1,n+1):
            if i ==1:
                res+= 10
            else:
              
                temp = i-1
                val = 9
                ans = 1 
                while(temp):
                 
                    ans *=  val
                    val-=1
                    temp-=1 
                res +=  ans*9

        return res 