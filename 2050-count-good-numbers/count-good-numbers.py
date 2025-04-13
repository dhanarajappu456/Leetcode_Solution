class Solution:
    def countGoodNumbers(self, n: int) -> int:


        def pow_(x,n):
            if n==0:
                return 1
            elif n  ==1:
                return x

            ans  = pow_(x, n//2)

            if n%2 ==1:
                return ((ans*ans)%md*x)%md
            else:
                return (ans*ans)%md

            

        md  = 10**9 + 7
        ans  = 1
        even_pos  = math.ceil(n/2)
        odd_pos  =  n - even_pos
        ans  = ((pow_(5,even_pos))%md   * ( pow_(4, odd_pos ))%md ) %md
        return ans