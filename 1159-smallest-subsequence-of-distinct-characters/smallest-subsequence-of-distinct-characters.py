class Solution:
    def smallestSubsequence(self, s: str) -> str:


        stk  = []
        last_index = {c:i for i,c in enumerate(s)}
        for i, c in enumerate(s):
            if c in stk:
                continue
            while(stk  and stk[-1] and stk[-1]>c and last_index[stk[-1]]>i):
                stk.pop(-1)
            
            stk.append(c)

        return "".join(stk)
        