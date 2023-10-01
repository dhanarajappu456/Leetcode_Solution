class Solution(object):
    def reverseWords(self, s):
        #as we iterate through the given string , reverse each word
        n  = len(s)
        s = list(s)
        l=0 
        for r in range(n):
            #when we reach end of a word(delimiter is space), also note there is edge case , 
            #where the last word may not have white space following , so take that condition as well
            if s[r] == " " or r == n-1:
              
                temp_l= l
                temp_r = (r-1 if s[r]==" " else r )
                #2pointers - reversing 
                while(temp_l<temp_r):
                    s[temp_l],s[temp_r] = s[temp_r],s[temp_l] 
                    temp_l+=1
                    temp_r-=1

                
                l = r+1

        return "".join(s)