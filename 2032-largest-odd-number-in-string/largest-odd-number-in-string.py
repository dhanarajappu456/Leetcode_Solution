'''
#solution 1 
The idea is simple 

we need to find the right most odd digit i, and all digit to left of it is part of the number 
that is,  digits from 0 to i gives the greatest odd number
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        odd_rightmost_ind =-1
        n= len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2!=0:
                odd_rightmost_ind = i
                break
        return num[:odd_rightmost_ind+1]
            
            
            
        