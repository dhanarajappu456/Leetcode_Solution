

'''
tabulation - 
we start placing the stick from the right end , so that we are sure if a stick will be visible or not, by the permutaion of remaining stick , 
a) when we place tallest of the remainig stick at the current  position 

state transtion -> rec(n-1 , k-1) -> that is this particular stick is visible for sure so remaining k  to suffice is k-1

b)  if we place the remainng n -1 stickss then state transition happens as _> rec(n-1 , k) -> 
that is  this stick is not gooing to be visible for sure, since it would be blocked by some sticks in future (ie, to left of it ) so k to suffice is still k 

'''
from functools import lru_cache

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        # @lru_cache(None)
        # def rec(n,k):
            

        #     if n==0:
        #         return 1 if k ==0 else  0

        #     ans  =0
        #     ans = (ans +  ((n-1)%mod*rec(n-1,k)%mod)%mod  +   rec(n-1,k-1)%mod)%mod
        #     return ans 
            
           

        # return rec(n,k)

        
        dp = {}
        for i in range(1,n+1):
            dp[(i,0)] =0
        for j in range(1,k+1):
            dp[(0,j)] =0
        dp[(0,0)] =1

        
        for i in range(1,n+1):
            for j in range(1,k+1):
                ans = 0
                ans = (ans +  ((i-1)%mod*dp[(i-1,j)]%mod)%mod  +   dp[(i-1,j-1)]%mod)%mod
                dp[(i,j)]= ans 

        return dp[(n,k)]

                


'''
t n*k
s n*k 

'''
       