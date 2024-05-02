class Solution:
    def minLength(self, s: str) -> int:

        stk =[]

        for c in s :

            if stk and stk[-1] =="C" and c=="D":
                stk.pop(-1)
            elif stk and stk[-1] =="A" and c=="B":
                stk.pop(-1)
            else:
                stk.append(c)
        return len(stk)
        