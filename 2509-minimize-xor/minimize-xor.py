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
        ans  = 0
        while(ones and i<len(num1_b)):
            if num1_b[i] =="1":
                print(i)
                ans|= (1<<(m-1)-i)
                ones-=1
            i+=1
        mask = 1
        print("ones",ones)
        while(ones ):
            if (mask & num1) ==0:
                print(mask, "mask")
                ans|=mask
                ones-=1
            mask<<=1

        return ans

        




        return 0 