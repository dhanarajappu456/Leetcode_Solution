class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        

        '''


        rather than generating the string chain in forward , we generater in backward, so we might delete , on characater as the 

        chain progress, 

        for current word, we try removing each of the characer , and see if the word is present in the given list( for faster lookup, 
        we can use a hashmap , it maps the word to the inde, 


        overlapping subproblem , 

        since longest chain from  the same word not change and this may be called multiple times , we might cache the indices, 
        as we remove a character and get new word present in the list, we might get the index, from the hash map , 
        that we created, further which the recursion is called 


        the dfs is called for all the string in the word, with word being assumed as the beginning of the chain (rememeber chain is constructed from the end )



        )


        
        '''

        words.sort(key = lambda x: -len(x))
        map_   = { word :  i  for i,word  in enumerate(words)}
        @lru_cache
        def rec(ind):  #time n = 1000
            if ind<0:
                return 0 
            ans = 0 
            for i in range(len(words[ind])):  # 16 
                word = words[ind][:i] + words[ind][i+1:]  # #16 
                if  word in map_:
                    ans = max(ans,   1+ rec(map_[word]))
            return ans
        
        ans  = 1
        for i, word in enumerate(words):
            ans   =  max(ans, 1 + rec(i)) 
        return ans 


        '''
        time : 1000* 16*16 
        space ; stack space( n = 1000) + map space (n=1000)
        '''