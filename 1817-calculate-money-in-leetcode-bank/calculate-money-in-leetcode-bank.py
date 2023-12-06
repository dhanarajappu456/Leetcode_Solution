'''
solution1 - simultion

t n 
s 1
#solution 2 - using sum formula ap 

the total sum of  money deposited in each complete week given differ  by 7 

week1  - 28
week2  - 35
week3  - 42
    :
    :
    :

thus, it is about finding sum of total value for complete weeks using sum formula of ap, where start  term is 28
d =7 and number of terms need to be found by n//7

also there'll be a partial week , whose sum also need to be found with ap 
but there starting need to be foun which is number of complete week +1 

also d for he sequence is 1 and number of terms is got by n%7

t 1
s 1

'''

class Solution:
    def totalMoney(self, n: int) -> int:
        tot = n
        ans = 0
        #start and number of term for complete weeks
        a=28
        n = tot//7 
        
        #start and number of term for last incomplete week
        rem_start = n+1
        n_rem = tot % 7

        #summing all values in complete week and then the partial week

        ans  += n/2 *(2*28 + (n-1)*7)  
        
        ans  += n_rem/2* (2*rem_start + n_rem-1) 

        return int(ans)