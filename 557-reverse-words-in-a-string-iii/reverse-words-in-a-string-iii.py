class Solution(object):
    def reverseWords(self, s):
        
        n  = len(s)
        s = list(s)
        l=0 
        for r in range(n):

            if s[r] == " " or r == n-1:
              
                temp_l= l
                temp_r = (r-1 if s[r]==" " else r )
            
                while(temp_l<temp_r):
                    s[temp_l],s[temp_r] = s[temp_r],s[temp_l] 
                    temp_l+=1
                    temp_r-=1

                
                l = r+1

        return "".join(s)