class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1,stk2= [],[]

        for i,c in enumerate(s):
            if c=="#":

                if stk1:
                    stk1.pop(-1)
            else:
                stk1.append(c)

        
        for i,c in enumerate(t):
            if c=="#":

                if stk2:
                    stk2.pop(-1)
            else:
                stk2.append(c)
        
        return stk1==stk2
