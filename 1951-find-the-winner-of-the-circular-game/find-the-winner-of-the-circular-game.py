from collections import deque as dq 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:


        def rec(n,k):

            if n==1:
                return 0
            
            ind = rec(n-1,k)
            ind = (ind+k) % n

            return ind
        
        return 1+rec(n,k)