class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        
        
  
        res = 0
        '''
        i denote the number of digit in the number 
        '''
        for i in range(1,n+1):
            if i ==1:
                res+= 10
            
           
            else:

                '''
                for nums with number of digit >1 ,
                that is like 2 digit ,  digit number 
                the first msb position cant have  0
                rest position can have 0, 
                so we calcualte the computatation starting from the 2nd position from msb
                and at end of loop we multiply the ans by  9 , 
                that comes from the count of possible  number that can be placed at the 
                first msb position  
                '''
              
                temp = i-1
                val = 9
                ans = 1 
                while(temp):
                 
                    ans *=  val
                    val-=1
                    temp-=1 
                res +=  ans*9

        return res 