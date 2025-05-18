class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        #hamming distance
        '''
        words =
        ["adbe","acace"]
        groups =
        [2,2]
        '''
        def hamming(i,j,l):
            hamDist = 0 
            if len(words[i]) == len(words[j]):
                for k in range(l) :
                    if words[i][k]!= words[j][k]:
                        hamDist+=1
            return hamDist

        #this is the LIS template that we gonna try
        n = len(words)
        dp =     [  1 for i in range(n) ]
        parent = [ -1 for i in range(n) ]
        ans = []
        longest  = -1 
        long_end_ind =0 
        for i in range(n):
            j = i - 1 
            while(j>=0):
                if( ( hamming( j, i , len(words[i]) ) == 1  ) and ( groups[j] != groups[i]) ):
                    if dp[i] < 1+dp[j]:
                        dp[i] =  max(dp[i], 1+ dp[j])  
                        if longest < dp[i]:
                            long_end_ind  = i
                            longest = max (longest , dp[i] )
                        parent[i]  = j
                j-=1
        ind  = long_end_ind
        while(ind!=-1):
            ans = [words[ind]] + ans
            ind  = parent[ind]
        return ans

      
            
            
                        
        