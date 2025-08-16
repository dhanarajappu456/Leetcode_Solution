class Solution:
    def maximum69Number (self, num: int) -> int:
        n = len(str(num))

        for i in range(n):
            place_val = 10**(n-1-i)
            if (num//place_val)%10 == 6:
                num -= place_val*6 
                num+=  place_val*9
                return num
        return num
        