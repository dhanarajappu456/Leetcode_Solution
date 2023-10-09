class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        rev= str2[::-1]
        m,n  = len(str1) ,len(str2)
        dp = [[0 for j in range(n+1)]  for i in range(m+1)]
        
        ans =[]

        for i in range(1,m+1):
          
            for  j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    
                    dp[i][j] = 1+dp[i-1][j-1]
                else: 
                    dp[i][j] =max(dp[i-1][j] , dp[i][j-1])
         
        #print(dp)
            
   
        while(i>0 and j>0):

                if str1[i-1] == str2[j-1]:

                    
                    ans.append(str1[i-1])
                    i-=1
                    j-=1

                else: 
                    if dp[i-1][j]>=dp[i][j-1]:

                        ans.append(str1[i-1])
                        i-=1

                    else:           
                        ans.append(str2[j-1])
                        j-=1
        # print(i,j)
        while(i>0):
            ans.append(str1[i-1])
            i-=1

        while(j>0):
            ans.append(str2[j-1])
            j-=1
    
        return "".join(ans[::-1])

                        
                       


                    

        