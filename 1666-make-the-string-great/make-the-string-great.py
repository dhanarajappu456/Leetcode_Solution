class Solution:
    def makeGood(self, s: str) -> str:
        stk = []


        for c in s :
            if stk and ((ord(stk[-1])+32 ==ord(c)) or (ord(stk[-1])-32 ==ord(c))):
                stk.pop(-1)
            else:
                stk.append(c)

        return "".join(stk)