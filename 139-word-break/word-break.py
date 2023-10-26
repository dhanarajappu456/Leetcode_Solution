'''
tabulation 


the state dp[i] = indicate if we can partition the word from i to end , such that the all the words fall in the dictionary 
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        n = len(s) 
        dp = [False for i in range(n+1)]
        dp[n]= True

        wordDict  = set(wordDict)
        
        for st in range(n-1,-1,-1):

            for end in range(st,n):
                if s[st:end+1] in wordDict:  #this lookup takes length of substring time complexity = st-end+1
                    if dp[end+1]:
                        dp[st] = True
                        break
        return dp[0]


    '''
    t  n^2 (n= word length)
    s  n 

    '''
     