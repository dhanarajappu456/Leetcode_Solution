from collections import defaultdict as dict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        colors = []
        #create the color combination
        def rec(i,chosen):
            if i == m :
                colors.append(chosen)
                print(chosen)
                return 
            for col in "RGB":
                print("chosen" , chosen)
                if (chosen == "") or (chosen[-1] != col) :
                    rec(i+1,chosen+col)
        rec(0,"")
    
        def possible(col, pre):
            if pre == "":
                return True
            for i in range(m):
                if col[i]==pre[i]: 
                    return False
            return True
        memo = [[ -1  for j in range( len(colors) + 1)] for i in range(1000) ]

        mod  = 10**9+7
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


               









        





        
            
            




         

        