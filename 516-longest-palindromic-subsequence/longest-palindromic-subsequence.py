class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
            
        def longestCommonSubsequence(text1: str, text2: str) -> int:
        
        
            n,m = len(text1),len (text2)
            prev = [0 for i in range(m+1)]      
            temp =  [0 for i in range(m+1)]  
            for ind1 in range(1,n+1):
                temp =  [0 for i in range(m+1)]  
                for ind2 in range(1,m+1):
                    if text1[ind1-1] == text2[ind2-1]:
                        temp[ind2] = 1+ prev[ind2-1]
                    else:

                        temp[ind2]  = max( temp[ind2-1] ,prev[ind2])     
                
                prev = temp
               
            return prev[m]
            
        
        text1,text2 = s, s[::-1]
        return longestCommonSubsequence(text1,text2)
            
        
        
        
        