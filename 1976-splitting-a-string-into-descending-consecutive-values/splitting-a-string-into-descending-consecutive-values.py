class Solution:
    def splitString(self, s: str) -> bool:
        
        n  = len(s)
        def rec(ind, prev_val , parts):

            if ind  == n : 
                return parts>=2

            for i in range(ind,n):
                curr = int(s[ind:i+1]) 
                if parts ==0 or  curr == prev_val-1:
                    if rec(i+1, curr, parts+1):
                        return True
            return False
        return rec(0,-1, 0)



                