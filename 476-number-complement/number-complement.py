class Solution:
    def findComplement(self, num: int) -> int:
        ans   =  0 
        temp = num
        j = 0  
        while(temp):
            temp = temp>>1
            j+=1
      
        for i in range(j-1,-1,-1):
            ans = (ans << 1)
            if (num & (1<<i)) == 0  :

                ans |= 1
        return ans 
        