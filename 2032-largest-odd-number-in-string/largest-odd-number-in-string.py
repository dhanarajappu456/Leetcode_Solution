class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        odd_rightmost_ind =-1
        n= len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2!=0:
                odd_rightmost_ind = i
                break
        return num[:odd_rightmost_ind+1]
            
            
            
        