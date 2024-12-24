class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
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


        text1,text2 = str1,str2
        n,m = len(text1),len (text2)
        dp =  [ [0 for j in range(m)] for i in range(n)] 
        dp[0][0] = int(text1[0] == text2[0])
        for j in range(1,m):
            '''
            set if there is a match found previously 
            '''
            dp[0][j] =  dp[0][j-1]  or int(text2[j] == text1[0])
        for i in range(1,n):
           
            for  j in range(m):
                choice1 , choice2 , choice3  = 0,0,0
                if text1[i] == text2[j]:
                    choice1= 1 
                    if j-1>= 0 :
                        choice1 += dp[i-1][j-1]
                choice2 =  dp[i-1][j]
                if j-1>=0:
                    choice3 =  dp[i][j-1]
                dp[i][j] = max(choice1, choice2 ,choice3)
            

        i,j = n-1,m-1
        s = ""
        while(i>=0 and j>=0):
       
            if text1[i] == text2[j]:
    
                s  = text1[i] + s
                i-=1
                j-=1
            
            else:
                left ,top = -1,-1 
                if i-1 >=0 :
                    
                    top = dp[i-1][j]
                if j-1>=0 :
                 
                    left = dp[i][j-1]
                if top>=left:
                    s = text1[i] + s
                    i-=1
                else:
                    s = text2[j] + s
                    j-=1
            
       
        

        return text1[:i+1]+ text2[:j+1] + s 



                        
                       


                    

        