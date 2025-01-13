from collections import defaultdict as dict

class Solution:
    def minimumLength(self, s: str) -> int:
        chars_cnt = [0 for i in range(26)]
        n = len(s)
        min_len = n
        for i in range(n):
            c  = s[i]
            val  = ord(c)-ord('a')
            chars_cnt[val]+=1
            if chars_cnt[val] == 3:
                min_len -=2
                chars_cnt[val]=1
        return min_len
