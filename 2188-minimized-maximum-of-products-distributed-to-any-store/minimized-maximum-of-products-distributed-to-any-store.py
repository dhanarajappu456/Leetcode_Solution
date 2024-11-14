class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        ans = float("inf")
        def check(val):
            counts = 0 
            for q in quantities:
                counts += math.ceil(q/val)
            return counts <= n

        def binary():
            nonlocal ans
            l, h = 1 , sum(quantities) 
            while(l<=h):
                m  = (l+h)//2
                if check( m ):
                    h = m-1
                    ans  =  min(ans, h)
                else:
                    l = m+1 
        binary()
        return ans+1


        
