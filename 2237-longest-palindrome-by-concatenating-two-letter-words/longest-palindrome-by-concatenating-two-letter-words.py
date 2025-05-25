from collections import defaultdict as dict


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = dict(int)
        words_set = set(words)
        for w in words:
            cnt[w]+=1
        

        ans =  0
        for w in words:
            if (w==w[::-1]) :
                cnts = cnt[w]//2
                cnt[w] -= ( 2*cnts)
                ans += cnts*2*2
            elif (w[::-1] in words_set):
                cnts = min(cnt[w],cnt[w[::-1]])
                ans+= 2*2*cnts
                cnt[w] -= cnts
                cnt[w[::-1]] -= cnts
        for w in cnt:
            if w==w[::-1] and cnt[w]!=0:    
                ans+= 2
                break
        return ans
