
class Solution:
    def climbStairs(self, n: int) -> int:
        

        p =None
        p1 ,p2= 1,1 
        for i in range(2,n+1):

            p   = p1+p2

            p2,p1 = p, p2
        return p2