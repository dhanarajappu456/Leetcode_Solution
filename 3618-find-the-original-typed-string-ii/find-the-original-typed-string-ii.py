from collections import defaultdict as dict 
from functools import lru_cache
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod  = 10 **9 +7
        freq  = []
        count = 1
        total  = 1
        n = len(word)
        #time : n 

        if k > len(word):
            return 0
        for i in range(1,n):
            if word[i] == word[i-1]:
                count+=1
            else:
                freq.append(count)
                count  = 1
        freq.append(count)

         

        for count in freq:
            total  = (total%mod *count%mod)%mod
        
        #if the character of multiple occurence let at each halt be say z 
        # and z>=k then the total ans
        # product of freq of each such charcter
        if k<= len(freq):
            return total

        m  = len(freq)
        dp = [ [ -1 for j in range(k)] for i in range(m+1)]
        for j in range(k):
            dp[-1][j] = 1
        
        
        for i  in range(m-1,-1,-1):
            prefix = [ 0 for i in range(k)]
            sm  = 0
            for  _ in range(k):
                sm = (sm %mod + dp[i+1][_]%mod)%mod
                prefix[_] = sm
            for j in range(k-1,-1,-1):
                res = 0
                left , right = prefix[-1], prefix[-1]
                if j+freq[i] <k:
                    right = prefix[j+freq[i]]
                if j+1 <k:
                    left  =  prefix[j]
                res = right - left
                dp[i][j] = res
        invalid_count   = dp[0][0]
        return (total%mod - invalid_count  + mod)%mod




  

        