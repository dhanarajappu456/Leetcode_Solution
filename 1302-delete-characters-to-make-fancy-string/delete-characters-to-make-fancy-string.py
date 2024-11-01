class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_char  = -1
        cnt =0 
        ans  =  [ ]
        for c in s:
            if   prev_char == c :
                if cnt<2:
                    cnt+=1
                    ans.append(c)  
            else: 
                prev_char = c 
                ans.append(c)
                cnt=1 
        return "".join(ans)


        