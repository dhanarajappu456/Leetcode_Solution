class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans  = 0 
        def punishment(num):
            str_num_sqr = str(num*num)
            n = len(str_num_sqr)
            def rec(i , sum_):
                if i == n and sum_ == num :
                    return True
                for j in range(i,len(str_num_sqr)):
                    if rec(j+1, sum_ + int(str_num_sqr[i:j+1])): 
                        return True
                return False
            
            return rec(0,0)

        for i in range(1,n+1):
            if punishment(i):
                ans+= i * i 
        return ans 