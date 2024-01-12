class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        n = len(s)
        left = 0 
        right = 0 
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(n):
            
            if s[i] in vowel:
                right+=1
            if i+1 == n//2: 
                left = right
                right =0
        
        return left == right

        


        