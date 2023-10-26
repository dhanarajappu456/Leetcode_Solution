'''
tabulation 
the state dp[i] = indicate if we can partition the word from i to end , such that the all the words fall in the dictionary 
the same tabulation with same complexity , but instead of dictionary lookup we use trie
'''


class Node:

    def __init__(self):


        self.end=False
        self.dic  = {}

class Trie:
    def __init__(self):

        self.head =Node()

    def present(self,word):
        temp = self.head
        for ch in word:
            if ch not in temp.dic:
                return False
            temp = temp.dic[ch]
        
        return temp.end
    
    def insert(self,word):
        temp = self.head
        for ch in word:
            if ch not in temp.dic:
                temp.dic[ch] =Node()
            temp = temp.dic[ch]
        
        temp.end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        


        n = len(s) 
        dp = [False for i in range(n+1)]
        dp[n]= True
        wordDict  = set(wordDict)

        trie = Trie()
        '''insert all the words in wordsDict to trie)
        '''
        for word in wordDict:
            trie.insert(word)
        
        
        for st in range(n-1,-1,-1):
            for end in range(st,n):
                if trie.present(s[st:end+1] ): # this takes same time complexity as of dictioanry lookup , which is end-st+1, 
                    if dp[end+1]:
                        dp[st] = True
                        break
        return dp[0]


    '''
    t  n^2 (n= word length) + mk(creeating the triem of word dict , m = wordidct length , k = length of each word in worddict)
    s  n 

    '''
     