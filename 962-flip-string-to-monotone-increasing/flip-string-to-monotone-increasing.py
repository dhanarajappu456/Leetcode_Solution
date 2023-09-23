class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        '''
        efficient solution 

        as we iterate on the stirng ,   from beggining to current index, we will have the  minflips required to make it monotone , stored 
        in a "flip" variable


        
       
        
        at the end of the string we will have the minflips needed for the entire string

        method
        ____________________

        at any index we have 2 possibility ,  to make it one or 0 
        1) if we want  make current char to 0 , we also need to make all the previosu 1's to 0 
        that is why wee need to keep track of the 1's so far

        if current char is 0, then flips_needed  = prev_ones
        else, flips_needed = prev_ones+ 1

        2) to  make current character to 1 , we  already have the number of flips need to make all the chars till previosu index as 
        flip , 

        so if current char is 0 , then  total flips_needed is flip+1, 
        else flips_needed is flip

        so the min flip till the index, will be minimum of either of two

        ____________________


        '''


        prev_ones = 0
        flips  = 0 

        for i, c in enumerate(s):

            #if we decide to keep this as 0 

            flips_needed_0 = prev_ones + ( 1 if c=="1"  else 0 )

            #we dedide to keep  this as 1    

            flips_needed_1 = flips +  ( 1 if c=="0"  else 0 )

            flips = min( flips_needed_0, flips_needed_1)
           
            if c == "1":
                prev_ones+=1
        return flips





   

        