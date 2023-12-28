from collections import defaultdict as dict 
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        n = len(s)
        @lru_cache(None)
        def rec(i,prev_char,freq,k ):
            
            if i ==n:
                ans  = len(str(freq))
                if prev_char in "abcdefghijklmnopqrstuvwxyz":
                    if freq>1:
                     
                        return ans
                    else:
                  
                        return 0
                #when you could delete all chars with available k 
                return 0

            tk_ =float("inf") 
            not_ =float("inf")

            #tk
            if s[i] == prev_char:
                tk_ = rec(i+1,prev_char, freq+1,k)
            else:
                freq_len = len(str(freq))
                
                tk_ = 1 + rec(i+1,s[i] , 1, k)
                if freq>1:
                    tk_ += freq_len

            #not
            if k>0:
             
                not_ = rec(i+1,prev_char,freq,k-1)
            
         
            return min(tk_,not_)
        return rec(0,"-",0,k)