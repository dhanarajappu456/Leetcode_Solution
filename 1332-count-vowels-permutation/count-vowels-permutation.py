class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follow = {'':"aeiou",'a':"e",'e':"ai",'i':"aeou",'o':"iu",'u':"a"}

        memo ={}
        mod  = 10**9+ 7
        def rec(char,rem):

            if rem ==0:
                return 1


            if (char , rem ) in memo:
                return memo[(char, rem)]
            ans = 0

            for c in follow[char]:
             
                ans = (ans + rec(c,rem-1)%mod)%mod
            memo[(char,rem)] = ans
            return memo[(char, rem)]

        return rec("",n)
        