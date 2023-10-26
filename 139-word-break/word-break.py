'''

make all the possible  partition of the given word and check if any of them  gives all the word in the parition.

the state memo[i] = indicate if we can partition the word from i to end , such that the all the words fall in the dictionary 
'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        n = len(s) +1 
        self.memo =[-1 for i in range(n)]
        
        self.wordDict=wordDict
        self.s  = s
        if self.rec(0):
            return True
        return False
    




    def rec(self,ind):
        if ind == len(self.s):

            return True

        if self.memo[ind]!=-1 :

            return self.memo[ind]

        
        for i in range(ind,len(self.s)):
            if self.s[ind:i+1] in self.wordDict:

                if self.rec(i+1):
                    self.memo[ind] = True
                    return self.memo
       
        self.memo[ind] =False 
        return self.memo[ind]       

    '''
    t  n^2 (n =word length)
    s  n + aux , the memo  size and aux  space (n =word length )

    '''
     
                
                
                
                    