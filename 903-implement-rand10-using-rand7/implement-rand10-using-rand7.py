# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

'''

consider table of 7 x7 
    1  2  3  4  5  6  7
---------------------
1 |  1  2  3  4  5  6  7
2 |  8  9 10 11 12 13 14
3 | 15 16 17 18 19 20 21
4 | 22 23 24 25 26 27 28
5 | 29 30 31 32 33 34 35
6 | 36 37 38 39 40 41 42
7 | 43 44 45 46 47 48 49


#solution1 
one way is to generate a sum of numbers returned by calling rand7() two times -1 
but note that the sum got would be from 1 to 13, 
so we might add a loop to limit the number from only 1 to 10 , 

but for this to happen one of the dice value must be <=2 and other dice can be any value

 but to constrain one of the rand7() val returned to <=2 , we might need to make more calls

 solution 2

we generate two nums by calling rand7(), where each of the number denote the row and col in teh table, 
since we need uniform distribution , we only consider nums from 1 to 40 
then we map this val got to a num from 1 to 10 
the formula is val%10 if the val not mult(10) 
else if it is mult(10) we return 10 

thus each numb from 1 to 10 has equal prob = 4/40 =1/10

ie 1 got from (1,11,21,31,)
   2 from (2,12, 22, 32)
   3 from (3, 13, 23, 33)

   
   .
   .
   . 
   and so on 

'''
import random 
class Solution:
    def rand10(self):
        
        while(True):
            r = random.randint(1,6)
            c = random.randint(1,7)
            val = (r-1)*7+c
            if val<=40:
                break
        
        ans = val%10
        if ans ==0:
            return   10
        return ans

        
        
        