class Solution:
    def firstPalindrome(self, words: List[str]) -> str:


        def pali(s):
            n =len(s)
            i,j = 0,n-1

            while(i<=j):
                if s[i] != s[j]:
                    return False

                i+=1
                j-=1
            return True
        
        for s in words:
            if pali(s):
                return s
        return ""
            