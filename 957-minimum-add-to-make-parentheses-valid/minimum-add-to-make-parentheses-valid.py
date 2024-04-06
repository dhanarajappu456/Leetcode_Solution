class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stk = []
        for c in s :
            if c == ")":
                if stk and stk[-1] == "(":
                    stk.pop(-1)
                else:
                    stk.append(")")
            else:
                stk.append("(")
        return len(stk)
            