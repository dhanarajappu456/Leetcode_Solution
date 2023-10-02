class Solution(object):
    def winnerOfGame(self, colors):
        '''

        note that , the possibility of favourable   A or B is not going to be increased 

        therefore it is better to count number of A and B  the alice and bob can get in the initial configuraton 
        and determine which is greater and that plaer wins for sure 
        '''
        n =len(colors)
        A,B = 0,0
        for i in range(1,n-1):
            c = colors[i]
            if  c== "A" :
                if i-1>=0 and colors[i-1] == "A" and i+1<=n-1 and colors[i+1] == "A":
                    A+=1 
            if c== "B":
                if i-1>=0 and colors[i-1] == "B" and i+1<=n-1 and colors[i+1] == "B":
                    B+=1 
        return A>B


        