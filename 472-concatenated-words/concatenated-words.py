class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = set(words)
        def wordPresentChecker(word):
            n = len(word)
            dp = [False for i in range(n+1)]
            dp[n] = True
        
            for ind in range(n-1,-1,-1):
                for j in range(ind,n):
                    if (word[ind:j+1]!= word )and (word[ind:j+1] in words):
                        if word == "cat":
                            print(ind, j)
                        if dp[j+1]:
                            dp[ind] = True
                            break
            return dp[0]
        

        m = len(words)
        ans = []
        for word in words: 
            present =wordPresentChecker(word)
            if present:
                ans.append(word)
        return(ans)


            
        