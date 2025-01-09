class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:
            if len(pref)<= len(word):
                m = len(pref)
                if word[:m] == pref:
                    cnt+=1
        return cnt