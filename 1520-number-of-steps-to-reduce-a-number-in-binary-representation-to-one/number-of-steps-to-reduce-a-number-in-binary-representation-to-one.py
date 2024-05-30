class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        l = n-1
        count =0 
        carry = 0 
        while(l>=0 ):
            #reached value 1, so stop 
            if( l == 0 )and (carry ==0):
                break
            if ((int(s[l]) +  carry ) == 0) and  (carry ==1):
                count +=1
                carry =1 
            elif ((int(s[l]) +  carry ) == 0) and  (carry ==0):
                carry = 0
                count+=1
            elif ((int(s[l]) +  carry ) == 1):
                count+=2
                carry =1 
            elif (int(s[l]) +  carry ) == 2:
                count+=1
                carry  = 1
            
            

      
           

            l-=1
   
        return count
        