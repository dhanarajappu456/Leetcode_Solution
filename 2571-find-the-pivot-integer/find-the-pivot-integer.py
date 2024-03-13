import bisect

class Solution:
    def pivotInteger(self, n: int) -> int:
        '''
        solution 3 
       using binary search--

       from the equation of solution 2 we  know x == totsum^0.5
       or  x**2  = totsum

       we use this equation to find the x 


        
        '''
        tot = n*(n+1)//2
        l,r =1,n

        while(l<=r):
            m =(l+r)//2
            if m**2 == tot:
                return  m
            elif m**2< tot:
                l=m+1
            else:
                r=m-1
        return -1
            
        