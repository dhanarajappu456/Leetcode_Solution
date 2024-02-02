
'''
fix a digit at msb from 1 to 9 then start creating the number by appending the lsb digit+1
in a recurisive fashion

t 9*9
s 9(const)

'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans =[]
        def rec(prev):

            if low<=prev<=high:
                ans.append(prev)
            if prev>high:
                return 
            if prev%10<=8:
                rec(prev*10 + prev%10+1)
        for i in range(1,10):
            rec(i)
        ans.sort()
        return ans