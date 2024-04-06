class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        open_extra,closed_extra = 0,0
        for c in s :
            if c == ")":
                if open_extra>0:
                    open_extra-=1
              
                else:
                    closed_extra+=1
            else:
                open_extra+=1
        return open_extra + closed_extra
            