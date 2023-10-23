class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
       
        pos=0
        onePos = -1
        numberOfOnes = 0
        while(n):
            
            if (n &1 ):

                print("1",n , pos)

                numberOfOnes += 1
                onePos = pos
            pos+=1
            if numberOfOnes>1:
                return False
            n>>=1
            print(n)

        return (numberOfOnes == 1) and (onePos%2 ==0)


        

    
        