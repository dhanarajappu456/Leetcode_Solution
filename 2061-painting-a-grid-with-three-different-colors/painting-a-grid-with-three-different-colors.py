from collections import defaultdict as dict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        colors = []
        #create the color combination
        #this create the color combination column wise , 
        #since the m value is just 5 at max length of each of this combo can
        #be 5


        #t : 3**m  , which at max , = 3**5 
        #s : i = is the aux space
        def rec(i,chosen):
            if i == m :
                colors.append(chosen)
                return 
            for col in "RGB":
                if (chosen == "") or (chosen[-1] != col) :
                    rec(i+1,chosen+col)
        rec(0,"")
        #this check if the current chosen color and the previous chosen 
        #colors can be chosen , by checking if there is same color in the
        #adjacent region
       
        def possible(col, pre):
            if pre == "":
                return True
            for i in range(m):
                if col[i]==pre[i]: 
                    return False
            return True
        memo = [[ -1  for j in range( len(colors) + 1)] for i in range(1000) ]

        mod  = 10**9+7


        # t : 1000 x 3**5  = 1000 x 100 = 10^5
        # s: 1000 * 3**m   = 1000 x 100 = 10^5
         # the state indicate , the number of ways of coloring 
         # given the col is the current column for which the color is 
         #to be chosen , and the ind indicate the index of color chosen
         #from the colors array
        def possibilities(col,ind):
            if col == n:
                return 1 
            if memo[col][ind] != -1:
                return memo[col][ind]
            ans  = 0
            for i in range(len(colors)):
                if ind== 0 or possible(colors[i], colors[ind-1]):
                    ans = ( ans + possibilities(col+1, i+1) %mod ) % mod
            memo[col][ind] =  ans

            return memo[col][ind]
        return possibilities(0,0)


               









        





        
            
            




         

        