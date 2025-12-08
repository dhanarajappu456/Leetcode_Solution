class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0 
        for a in range(1,n+1):
            for b in range(1,n):

                # a and b should be such that , the sum of their sqaures should be less than n**2
                # and also , a perfrect square,  which is what the condition is testing
                if  a!=b and  ( a**2 +b**2)  <= n**2    and  ( int(math.sqrt(a**2 +b**2))  ==  math.sqrt(a**2 +b**2)):
                    ans+=1
        return ans


        