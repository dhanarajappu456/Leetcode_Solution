class Solution:
    def minSwaps(self, s: str) -> int:

        stk  = [ ]


        for c in s: 
            if stk and stk[-1] == "[" and c =="]":
                stk.pop(-1)
            else:
                stk.append(c)
        return math.ceil((len(stk)//2)/2)