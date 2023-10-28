class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # '''
        # approach 1 - memoised dfs solution 
        # we check if we can split the word in to two(pref and suff / firshalf and second half), 
        # we check if pref and suff exist in the wordSet, 
        # there can be other situation ,when the pref is in the set, but suff not, so we need to call the rec function for suff further 


        # '''


        # wordSet = set(words)
        # @lru_cache(None)
        # def isConcatenated(word):
        #     m  = len(word)
        #     for i in range(m):#m
        #         pref = word[:i+1]  #
        #         suff  = word[i+1:]  # both slicing takes o(m), length of word

        #         if (pref in wordSet  and suff in wordSet ) or (pref in wordSet and isConcatenated(suff)): 
        #             return True
        #     return False

        # ans  =[]
        # for word in words:#n
        #     if isConcatenated(word):
        #         ans.append(word)
        # return ans
        
        # '''
        #  non memoised solution 
        #  t expo
        #  s aux space(length of word) , the list ans space is neglected

        #  memoised 
        #     t n *(m^2*m) = n*m^3  ,  2 for loop inside the rec takes m^2 , then the m for the number of  times the isconcatenated s called at worst
        #       = 10^4 * (30^3) = 10^7
        #      s aux space(length of word) , + mmeo space(n )



        # '''
      


          




        #solution 2 - similar to the dp problem - word break




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
        # t :n*(m^2), n =  length of words, nm= length of each word = 10^4 *(10^2)
        # s : n + m (converting the words list to set and the dp size) 




            
        