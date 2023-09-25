class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_=0
        for i in range(len(s)):
            xor_^=ord(s[i])^ord(t[i])
        return(chr(xor_^ord(t[-1])))