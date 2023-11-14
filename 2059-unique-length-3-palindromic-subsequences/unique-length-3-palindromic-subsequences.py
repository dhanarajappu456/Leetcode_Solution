from collections import defaultdict as dict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        prev  = set()
        ans  = dict(set)
        lastIndex = dict(int)

        for i,c in enumerate(s):
            lastIndex[c]= i 


        for i,c in enumerate(s):
            
            for endChar in "abcdefghijklmnopqrstuvwxyz":
                if endChar in prev and lastIndex[endChar]>i:
                    ans[c].add(endChar)
            
          
            prev.add(c) 
        
        res =0 
        for c in ans:
            res += len(ans[c])
        return res 
        
        
        
        
        