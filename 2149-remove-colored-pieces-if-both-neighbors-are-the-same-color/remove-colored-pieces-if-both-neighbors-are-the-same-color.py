class Solution(object):
    def winnerOfGame(self, colors):
        
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


        