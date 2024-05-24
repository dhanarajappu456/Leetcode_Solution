import heapq as h 

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        chars = Counter(letters)
       
        print(chars)

        def possible(word):
            taken = defaultdict(int)
            ans = 0 
            for c in word:
                if c in chars:
                    chars[c]-=1
                    if chars[c] ==0:
                        chars.pop(c)
                    ans+= score[ord(c)-ord('a')]
                    taken[c]+=1   
                else:
                    for c in taken:
                        chars[c]+= taken[c]
                    return -1
            return ans

        
        def rec(i):
            if i == len(words):
                return 0

            tk_ = 0
            not_ = 0
            scr = possible(words[i])
            if scr>=0:

                tk_  = scr+rec(i+1)

                for c in words[i]:
                    chars[c]+=1
            not_ = rec(i+1)
            return max(tk_ ,not_)
        return rec(0)