class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:


        leftMost = {chr(97+i):-1 for i in range(26)}
        ans =-1
        n = len(s)
        for i in range(n):

            if leftMost[s[i]]!=-1 :

                ans = max(ans,i-leftMost[s[i]]-1)
            if leftMost[s[i]]==-1:
                leftMost[s[i]]=i

        return ans

        