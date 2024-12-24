class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        n,m = len(text1),len (text2)
        # memo = [[-1 for i in range(m+1)] for j in range(n+1)]
        # def rec(ind1,ind2):
        #     if ind1==0 or ind2 ==0:
        #         return 0
        #     if memo[ind1][ind2]!=-1:
        #         return memo[ind1][ind2]
        #     if text1[ind1-1] == text2[ind2-1]:
        #         memo[ind1][ind2]   = 1+ rec(ind1-1,ind2-1)
        #     else:
        #         memo[ind1][ind2] = max(rec(ind1-1, ind2), rec(ind1, ind2-1))
        #     return memo[ind1][ind2]
        # return rec(n,m)



        prev = [0 for j in range(m)] 
        prev[0] = int(text1[0] == text2[0])
        for j in range(1,m):
            '''
            set if there is a match found previously 
            '''
            prev[j] =  prev[j-1]  or int(text2[j] == text1[0])
        for i in range(1,n):
            curr = [0 for j in range(m)] 
            for  j in range(m):
                choice1 , choice2 , choice3  = 0,0,0
                if text1[i] == text2[j]:
                    choice1= 1 
                    if j-1>= 0 :
                        choice1 += prev[j-1]
                choice2 =  prev[j]
                if j-1>=0:
                    choice3 =  curr[j-1]
                curr [j] = max(choice1, choice2 ,choice3)
            prev =  curr
        return prev[m-1]

                





            
            
            
        