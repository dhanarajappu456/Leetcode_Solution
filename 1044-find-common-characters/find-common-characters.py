class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(97,97+26):

            ch = chr(i)
            occur = 500
            for w in words:
                occur = min(occur,w.count(ch))
            if occur !=0:
                res= [ch]*occur
                ans.extend(res)
        return ans
        