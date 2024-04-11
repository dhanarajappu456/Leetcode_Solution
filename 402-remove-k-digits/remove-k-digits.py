class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stk  = []
        cnt =k
        for c in num:


            while(stk and stk[-1]>c and cnt>0):
                cnt-=1
                stk.pop()

            stk.append(c)

        while(cnt):
            stk.pop()
            cnt-=1
     
        ans  =  "".join(stk)
        ans = ans.lstrip("0")
        return  "0" if  ans  =="" else ans 
