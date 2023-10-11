class Solution:
    def countVowelPermutation(self, n: int) -> int:
        follow = {'':"aeiou",'a':"e",'e':"ai",'i':"aeou",'o':"iu",'u':"a"}
        mod  = 10**9+ 7

        #memoisation
        # memo ={}
      
        # def rec(prevChar,rem):

        #     if rem ==0:
        #         return 1


        #     if (prevChar , rem ) in memo:
        #         return memo[(prevChar, rem)]
        #     ans = 0

        #     for c in follow[prevChar]:
             
        #         ans = (ans + rec(c,rem-1)%mod)%mod
        #     memo[(prevChar,rem)] = ans
        #     return memo[(prevChar, rem)]

        # return rec("",n)


        #tabulation
        
        charMap  = {'a':0 , 'e':1, 'i':2,'o':3,'u':4}
        dp =  [1,1,1,1,1]

        for rem in range(1,n):
            temp  = [0 for i in range(5)]
            for prevChar in "aeiou":
                prev = charMap[prevChar]
                ans = 0
                for c in follow[prevChar]:
                    val  = charMap[c]
                    ans = (ans + dp[val]%mod)%mod
                
                temp[prev] = ans 
            dp = temp
        print(dp)     
        return sum(dp) % mod
                 

                

            
        