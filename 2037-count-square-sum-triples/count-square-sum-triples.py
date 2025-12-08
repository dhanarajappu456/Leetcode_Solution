class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0 
        for i in range(1,n+1):
            for j in range(1,n):
                if  i!=j and  ( i**2 +j**2)  <= n**2    and  ( int(math.sqrt(i**2 +j**2))  ==  math.sqrt(i**2 +j**2)):
                    ans+=1
        return ans


        