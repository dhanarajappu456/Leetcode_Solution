class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        large  = ""
        small =""
        large_val  =  0
        small_val  =  0
        if x>y:
            large ="ab"
            small = "ba"
            large_val  = x
            small_val  = y
        else:
            large  = "ba"
            small = "ab"
            large_val  = y
            small_val  = x



        stk = []
        ans = 0
        for c in s:
            if stk and stk[-1]+c == large:
                stk.pop(-1)
                ans += large_val
            else:
                stk.append(c)
        stk1 =  []
        for c in stk:
            if stk1 and  stk1[-1]+c == small:
                stk1.pop(-1)
                ans += small_val
            else:
                stk1.append(c)
            


        return ans 
        