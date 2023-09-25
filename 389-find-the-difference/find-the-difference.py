class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        sl =list(s)
        sl.sort()
        tl = list(t)
        tl.sort()

        for i in range(len(sl)):

            if tl[i]!=sl[i]:
                return tl[i]
        return tl[-1]
        