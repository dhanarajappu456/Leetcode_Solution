class Solution:
    def reverseParentheses(self, s: str) -> str:

        n = len(s)
        i=  0

        def rec():
            nonlocal i
            ans = ""
            while i<n and s[i]!=')':
                if s[i]!= "(":
                    ans =  ans + s[i]
                elif s[i] =="(":
                    i+=1
                    res =  rec()
                    i+=1
                 
                    ans =ans + res

                    continue
            
                i+=1
              
            if i<n and s[i] ==")":
                
                ans= ans[::-1]
                print(ans)

           
         

            return ans
        
        return rec()