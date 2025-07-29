from collections import defaultdict as dict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last_occ = dict(int)
        for i,c in enumerate(s):
            last_occ[c] = i
        prev  = set()
        mid  = set()
        ans = set()
        for i,c in enumerate(s):
            for j in range(26):
                ch = chr( ord('a') + j)
                if (last_occ[ch] > i  ) and (ch in prev):
                    ans.add(ch+c+ch)
            prev.add(c)
        return len(ans)
            
             
        