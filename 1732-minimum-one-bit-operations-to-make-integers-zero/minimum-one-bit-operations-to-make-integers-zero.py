import math as m 
'''
solution 1 

the question is tricky , just try break ing the problem


lets consider n as pow of 2

say 4

making it to 0

100
101
111
110
010
011
001
000

here you can see  to reduce 4 to 0 , the ans is :  we need 2^(2+1)-1, where 2 in the power is the position of msb in 4 .

Also one thing to note is it covers entire binary number in the range 000 to 111 in its path , 

so if the question were to reduce number say 111 , ans is , instead of jumping from 100 we took shortuct ,  to jump from 111 to  000, so ans to this is :

ans = (tot jump from 100 to 000) - (jump from 100 to 111, which is same as jump from 111 to 100  , which is same as jumping from 11[next bits of msb bit of 111]  to 00, this  a new subproblem now )
    
you can make the suproblem call (from   11 to 00   )by extracting 11 from 111 using 111^100


T LOGN  EACH SUBPROBLEM REDUCE THE N BY 2 
S LOGN

solution 2

gray code

gray code representation of binary numbers are nothing but each of  the gray code representation of binary numbers differ by just a single position


bin and gray representation of numbers from 0 to 7 

you can see adjacent gray codes differ by single position 
dec	Binary	Gray Code
0	000	    000
1	001	    001
2	010	    011
3	011	    010
4	100	    110
5	101	    111
6	110	    101
7	111	    100

you can see here in the graycode column  it  also represent the number of  steps to change the 100(4) to 000(0)

so basically for a given n if we find the path to make it 0 ,it  is the number jumps to reach from n to 0  where n and 0 is in   grey code representation , essentially if an n is given we need to find index if number in the gray code chart , or index is nothing but  binary value corresponding to n

learn how number is converted from bin to grey and grey to bin 

https://docs.google.com/document/d/1QBBxvdX9Ohm6_ldaJfZvqqFAZTpwpvMJwIka0LaeuIc/edit


t logn
s  1 




'''

#solution 1 
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         #THIS CALUCLTATION IS O(1)
#         def MSB(n):
            
#             msb  = m.floor(m.log(n, 2 ))
#             return msb 

#         #CALCULATE  NUMBER OF STEPS TO JUMP FROM N TO 0
#         def rec(n): #LOGN

#             #return 0
#             if n ==0 :
#                 return 0
            
#             #if n is pow of 2
#             if n-1 == 0 :
#                 return 2**(MSB(n))
#             else:
                
#                 return 2**(MSB(n)+1) - 1   -  rec(2**MSB(n)^n)

#         return rec(n)


#solution 2 
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
        #eachposition in the  binary representaion is xor of all the bits from 0th index to that particular position 
        ans  = 0 
        while(n):
            ans  = ans^n
            n>>=1
        return ans
        


        
   