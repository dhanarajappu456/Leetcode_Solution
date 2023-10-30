
#idea is simple we check all possibility of numbers i  possible to be splitted for num , ie, from(1 to num -1 )


#then recursively call the function for (num-i)



class Solution:
   
    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def rec(n):

            if n ==1:
                return 1
            ans  =  0 
            for i in range(1,n+1):

                ans  = max(ans, i*max(n-i, rec(n-i)))
            return ans
        
        return rec(n)

        