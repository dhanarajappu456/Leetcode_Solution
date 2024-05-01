class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:


    
        pref =""
        suff = ""
        for i,c in enumerate(word):
            pref=  c+ pref
            if c == ch:
                suff=word[i+1:]
                return pref+suff
        return word
        
        