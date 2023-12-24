class Solution:
    def minOperations(self, s: str) -> int:

        opt1, opt2 =0, 1
        min1 ,min2  = 0,0
        n =len(s)
        for i in range(n):

            if int(s[i])!=opt1:
                min1+=1
            
            if int(s[i])!=opt2:
                min2+=1
          
            opt1 = 1-opt1
            opt2 = 1-opt2 
            
        return min(min1, min2)
