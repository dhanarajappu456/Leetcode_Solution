class Solution:
    def nearestPalindromic(self, n: str) -> str:


        #possible candidates are 
        '''
        1. reversing first half and appending it to the first half let it be num1
        2.  then subtracting 1 from the middle digit of num1 , let it be num2 
        3.  then adding 1 to  the middle digit of num1 , let it be num3
        4. if n is 9, or 99, 999 , then ans is 10^(numbe of digit in n)+1 , let it be num4
         5.. if n is 10, or  101 , 1001 , then ans is 10^(numbe of digit in n -1)+1 , let it be num4
        '''





        def func(first_half , is_even):
            res = first_half
            if not(is_even):
                first_half //= 10

            while(first_half):
                dig = first_half%10
                res = res*10 + dig
                first_half //= 10 
            
            return res 

            

            
            



        
        diff = float("inf")
        ans  =  float("inf")

        candidates  =  []
        mid  = len(n)//2
        half_len   =  mid if len(n)%2==0  else mid + 1 
        first_half  = int( n[:half_len])
        is_even = len(n)%2 == 0 
        num1  = func(first_half , is_even )
        num2  = func(first_half-1 , is_even )
        num3  = func(first_half+1 , is_even )
        num4  = 10**len(n)+1
        num5  = 10**(len(n)-1) -1 


        candidates = [num1, num2, num3 , num4 , num5 ]
       
        #checking the best ans
        n  = int(n)
        for num in candidates :
            if num == n :
                continue
            if abs(n - num) < diff :
                diff =   abs(n - num)
                ans = num
            if abs(n- num) == diff :
                
                ans = min(ans , num )
        return str(ans) 
         


        










        