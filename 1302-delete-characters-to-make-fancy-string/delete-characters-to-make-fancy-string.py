class Solution:
    def makeFancyString(self, s: str) -> str:
        ans  =""
        for i,c in enumerate(s):
           
            if (i>=2) and (ans[-1]==c) and( ans[-2]==c) :
              
                continue 
            ans+= c 
        return ans
        