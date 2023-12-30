'''

Idea is simple since we can move any char from any position to any position 

the thing is count of any char across all words must be multiple of number of words, 
then only we can atleast make them equal 

t  w*c = 100*100
s  charmap  = 26

'''

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