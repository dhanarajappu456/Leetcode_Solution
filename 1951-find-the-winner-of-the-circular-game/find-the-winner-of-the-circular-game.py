from collections import deque as dq 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:



        
        def rec(n,k):
            '''
            when single element , which is winner , index of it is 0
            '''
            if n==1:
                return 0
            
            ind = rec(n-1,k)
            '''
            index of winner among n element is, k more  than index of it 
            when among n-1 elements
            '''
            ind = (ind+k) % n

            return ind
        '''
        at end the value of ans is 1 more than index at which it stays
        '''
        return 1+rec(n,k)