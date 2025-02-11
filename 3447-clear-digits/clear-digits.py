class Solution:
    def clearDigits(self, s: str) -> str:

        stk = []
        for c in s:
            if c.isdigit()  and stk and  stk[-1].isalpha():
                stk.pop(-1)
            else:
                stk.append(c)

        return "".join(stk )

            
        
        