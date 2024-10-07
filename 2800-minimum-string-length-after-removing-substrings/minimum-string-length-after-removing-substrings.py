class Solution:
    def minLength(self, s: str) -> int:
        stk  =[]
        for c in s :
            if c == "B":
                if stk and stk[-1] == "A":
                    stk.pop(-1)
                else:
                    stk.append(c)
            elif c == "D":
                if stk and stk[-1] == "C":
                    stk.pop(-1) 
                else:
                    stk.append(c)
            else:
                stk.append(c)
         
        return len(stk)

