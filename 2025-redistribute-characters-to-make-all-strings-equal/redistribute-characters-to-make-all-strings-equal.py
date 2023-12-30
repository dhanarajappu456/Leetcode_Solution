from collections import defaultdict as dict 

class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        mp =dict(int)
        n  = len(words)
        for word  in words:
            for c in word:

                mp[c]+=1 
    
        for c in mp:
            if mp[c]%n!=0:
                return False
        return True