class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = set(words)
        #this is dp problem word break 
        #https://leetcode.com/problems/word-break/description/
        def wordPresentChecker(word):
            m = len(word)
            dp = [False for i in range(m+1)]
            dp[m] = True
        
            for ind in range(m-1,-1,-1):
                for j in range(ind,m):
                    #check edge case when the  entire partion is equal to the word itself, 
                    if (word[ind:j+1]!= word )and (word[ind:j+1] in words):
                        if dp[j+1]:
                            dp[ind] = True
                            break
            return dp[0]
        

    
        ans = []
        for word in words: 
            present =wordPresentChecker(word)
            if present:
                ans.append(word)
        return(ans)


            
        