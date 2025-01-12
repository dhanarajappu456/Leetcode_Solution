class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2!=0:
            return False
        open,close=0,0
        for i,c in enumerate(s):
            
            if c == "(" or locked[i] =="0":
               open+=1
              
            else:
                open-=1
            if open<0:
                return False
        n = len(s)
        open,close=0,0
        for i in range(n-1,-1,-1):
            c = s[i]
            if c == ")" or locked[i] =="0":
               close+=1
              
            else:
                close-=1
            if close<0:
                return False    
        return  True

        
                    
                        
        