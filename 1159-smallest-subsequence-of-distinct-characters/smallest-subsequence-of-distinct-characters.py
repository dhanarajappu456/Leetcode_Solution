
'''

'''

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk  = []
        last_index = {c:i for i,c in enumerate(s)}
        for i, c in enumerate(s):
            #skip curr char if already in the stk
            #example s= bcabd, 
            #when at second b we need to consider it so continue
            if c in stk:
                continue
            #if top char come after the curr char , then pop it 
            while(stk  and stk[-1] and stk[-1]>c and last_index[stk[-1]]>i):
                stk.pop(-1)
            
            stk.append(c)

        return "".join(stk)
        