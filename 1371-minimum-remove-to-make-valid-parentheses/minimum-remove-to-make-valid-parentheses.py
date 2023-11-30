class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stk = []
        n = len(s)

        for i in range(n):

            if s[i]  =="(":
                stk.append(("(",i))
            elif s[i ] ==")":
                if stk  and stk[-1][0] =="(":
                    stk.pop(-1)
                else:
                    stk.append((")",i))

        #stk contain brackets and their indices that have no matching brackets, 
       
        #so need to be removed
        #the set stores indices of brackets to remove , which we neglect while taking chars to ans
        remove_able  = set(i for brk, i in stk)

        ans = []
        for i in range(n):
            if  i not in   remove_able:
                ans.append(s[i])
        return "".join(ans )


                


        