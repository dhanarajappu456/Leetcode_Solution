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
            #as soon as there are 3 chars available , we can delete the left
            #and right chars, keep the middle one 
            if chars_cnt[val] == 3:
                min_len -=2
                #persisting the middle char and assumed to moved to left most 
                #postition in the 3 position
                chars_cnt[val]=1
        return min_len
