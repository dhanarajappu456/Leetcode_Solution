class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        w = word
        ans = 0 
        while(len(w)<=len(sequence)):
            if w in sequence:
                ans +=1
            w+= word
        return ans 

