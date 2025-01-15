class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #1.count the number of 1's in num2
        #2.be greedy to unset the set bit in num1 
        #and generate the x such that

        num2_b = bin(num2)[2:]
        
        num1_b = bin(num1)[2:]
        m  = len(num1_b)
        n = len(num2_b)
        ones = num2_b.count("1")
        i = 0
        x  = 0
        #generating the number x, such that , msb 1's in num1 is
        #unset

        while(ones and i<len(num1_b)):
            if num1_b[i] =="1":
                x|= (1<<(m-1)-i)
                ones-=1
            i+=1
        mask = 1
        #if there are remainining ones ,
        #then starting from lsb x should be such that, 
        #we need to set the 0 to 1 , in the num1
        while(ones ):
            if (mask & num1) ==0:
              
                x|=mask
                ones-=1
            mask<<=1

        return x
