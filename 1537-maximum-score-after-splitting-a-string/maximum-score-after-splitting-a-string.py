'''
solution 1 

bruteforce try all the splits as we iterate on the string 
then for each left and right split count zero and ones, 

t = n^2
s = 1 

#solution 2 - time optimised  -2 pass

the above solution can be optimised, 
the zeros in the left can be calculated as we iterate , 
and for the ones in the right side, we can just keep total ones count before hand and 
thus can calculate the ones in right side ( if we also have kept the count of ones in left side)
t n 
s 1
'''

#solution 3 - single pass, 

'''we want 
zero_left  = one_right 
= zero_left + (tot_ones - one_left)
= (zero_left - one_left)  + tot_ones
thus we just need to find max value of zero_left - one_left , 

and finally add the tot_ones'''

#solution 3 
class Solution:
    def maxScore(self, s: str) -> int:
        

        tot_ones = 0 
        score = -float("inf")
        l_zero,l_one = 0,0
        n = len(s)
        #since we need left and right to be non empty , we can't have right as empty, 
        #which happens when i ==n-1
        for i in range(n-1):

            if s[i] == '0':
                l_zero+=1
            else:
                l_one+=1

                tot_ones+=1
            print(l_zero - l_one)
            score = max(score ,  l_zero - l_one)
        #since last value was skipped in iteration 
        
        if s[-1]=='1':
            tot_ones +=1
      
        return score + tot_ones

            