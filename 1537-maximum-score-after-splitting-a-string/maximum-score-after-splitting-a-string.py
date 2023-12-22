'''
solution 1 

bruteforce try all the splits as we iterate on the string 
then for each left and right split count zero and ones, 

t = n^2
s = 1 

#solution 2 - time optimised 

the above solution can be optimised, 
the zeros in the left can be calculated as we iterate , 
and for the ones in the right side, we can just keep total ones count before hand and 
thus can calculate the ones in right side ( if we also have kept the count of ones in left side)
t n 
s 1
'''

#solution2 
class Solution:
    def maxScore(self, s: str) -> int:
        

        tot_ones = s.count('1')
        score = 0
        l_zero,l_one = 0,0
        n = len(s)
        #since we need left and right to be non empty , we can't have right as empty, 
        #which happens when i ==n-1
        for i in range(n-1):

            if s[i] == '0':
                l_zero+=1
            else:
                l_one+=1

            r_one = tot_ones - l_one
           
            score = max(score, l_zero+r_one)
        return score

            