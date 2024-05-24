

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        chars = Counter(letters)
        #checking if current word can be formed
        #if all chars in word still exist in letters
        def possible(word):
            taken = defaultdict(int)
            ans = 0 
            for c in word:
                #building the word by choosing a char
                if c in chars:
                    chars[c]-=1
                    if chars[c] ==0:
                        chars.pop(c)
                    ans+= score[ord(c)-ord('a')]
                    taken[c]+=1   
                #if there is no any char in letter to form word return score -1
                #and add back all chars chosen to counter map
                else:
                    for c in taken:
                        chars[c]+= taken[c]
                    return -1
            return ans

        #backtracking
        #take or skipc urrent word
        def rec(i):
            if i == len(words):
                return 0

            tk_ = 0
            not_ = 0
            #take
            scr = possible(words[i])
            if scr>=0:

                tk_  = scr+rec(i+1)
                #add back taken character to the counter map
                for c in words[i]:
                    chars[c]+=1
            #not tak
            not_ = rec(i+1)
            return max(tk_ ,not_)
        return rec(0)