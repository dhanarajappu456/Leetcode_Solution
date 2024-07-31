class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        #'"bbbababaa"'
        stk = []
        cnt=0
        for c in s:
            if stk and stk[-1]=="b" and c=="a":
                stk.pop(-1)
                cnt+=1
                continue
            stk.append(c)

        return cnt

            