class Solution:
    def minChanges(self, s: str) -> int:

        i =0 
        n= len(s)
        count = 0
        ans  = 0 
        while(i<n):

            if i>=1 and (s[i]!=s[i-1]):

                if count %2!=0:
                    ans+=1
                    count = 0
                else:
                    count = 1
            
            else:
                count+=1
            i+=1
        return ans
                

            
        return ans
        

        