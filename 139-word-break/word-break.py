'''

make all the possible  partition of the given word and check if any of them  gives all the word in the parition.

the state memo[i] = indicate if we can partition the word from i to end , such that the all the words fall in the dictionary 
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        n = len(s) 
        dp = [False for i in range(n+1)]
        dp[n]= True

        wordDict  = set(wordDict)
        
        for st in range(n-1,-1,-1):

            for end in range(st,n):
                if s[st:end+1] in wordDict:
                    if dp[end+1]:
                        dp[st] = True
                        break
        return dp[0]


    '''
    t  n^2 - dict length
    s  n^2 + aux 

    '''
     
                
                
                
                    