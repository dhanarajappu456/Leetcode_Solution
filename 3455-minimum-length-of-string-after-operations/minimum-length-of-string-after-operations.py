from collections import defaultdict as dict

class Solution:
    def minimumLength(self, s: str) -> int:
        chars_cnt = dict(int)
        n = len(s)
        for i in range(n):
            c  = s[i]
            chars_cnt[c]+=1
        min_len = 0 
        for c in chars_cnt:
            #if even number of a char is present , then at end
            # 2 of it will be left 
            if chars_cnt[c]%2  == 0: 
                min_len+=2
            else:
                #if odd number of char is present , then at end
                #1 of it will be left at the end
                min_len+=1
        return min_len
