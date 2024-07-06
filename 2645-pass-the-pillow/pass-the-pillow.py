class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = time//(n-1)

        '''
        forward
        '''
        if d%2==0: 
            return 1+time%(n-1)
        else:
            print("hi")
            return n- time%(n-1)

        