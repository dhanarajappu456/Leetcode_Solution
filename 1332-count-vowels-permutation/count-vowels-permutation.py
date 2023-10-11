class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follow = {'':"aeiou",'a':"e",'e':"ai",'i':"aeou",'o':"iu",'u':"a"}

        memo ={}
        mod  = 10**9+ 7
        def rec(prevChar,rem):

            if rem ==0:
                return 1


            if (prevChar , rem ) in memo:
                return memo[(prevChar, rem)]
            ans = 0

            for c in follow[prevChar]:
             
                ans = (ans + rec(c,rem-1)%mod)%mod
            memo[(prevChar,rem)] = ans
            return memo[(prevChar, rem)]

        return rec("",n)
        