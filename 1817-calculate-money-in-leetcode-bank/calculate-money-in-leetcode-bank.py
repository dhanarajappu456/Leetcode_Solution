'''
solution1 - simultion

'''

class Solution:
    def totalMoney(self, n: int) -> int:
        tot = n
        a=28
        n = tot//7 

        rem_start = n+1
        n_rem = tot % 7

        
        ans  = n/2 *(2*28 + (n-1)*7)  + n_rem/2* (2*rem_start + n_rem-1) 

        return int(ans)