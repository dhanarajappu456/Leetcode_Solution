class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(c**0.5)
        while(l<=r):
            val = (l**2 + r**2 )
            if (val )<c:
                l+=1
            elif val>c:
                r-=1
            else:
                return True
        return False


        