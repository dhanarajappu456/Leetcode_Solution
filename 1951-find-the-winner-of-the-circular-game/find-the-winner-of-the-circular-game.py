from collections import deque as dq 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:


        ind = 0
        for i in range(2,n+1):
            ind =  ind = (ind+k) % i
    
        return ind+1
        