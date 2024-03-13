class Solution:
    def pivotInteger(self, n: int) -> int:
        '''

        from equating the sum of 1...x element == sum of x..n elements
        we get  x = root(n*(n+1)//2


        
        '''
        tot = n*(n+1)//2
        for i in range(1,n+1):
            
            if i == tot**(0.5):

                return i
        return -1