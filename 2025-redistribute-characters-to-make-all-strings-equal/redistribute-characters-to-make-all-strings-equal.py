from collections import defaultdict as dict 

class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        chars_count =[0 for i in range(26)]
        n  = len(words)
        for word  in words:
            for c in word:

                chars_count[ord(c)-97]+=1 
    
        for count in chars_count:
            if count%n!=0:
                return False
        return True