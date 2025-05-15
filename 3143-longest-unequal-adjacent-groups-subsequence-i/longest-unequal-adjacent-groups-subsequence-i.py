class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = -1
        ans  = []
        n = len(words)
        for i in range(n):
            if groups[i]!=prev:
                ans.append(words[i])
                prev = groups[i]
        return ans