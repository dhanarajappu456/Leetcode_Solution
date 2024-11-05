class Solution:
    def minChanges(self, s: str) -> int:

        i =0 
        n= len(s)
        count = 0
        ans  = 0 
        while(i<n):
            #mismatch from same set of chars seen so far
            if i>=1 and (s[i]!=s[i-1]):
                #combine current char to the grp 
                if count %2!=0:
                    ans+=1
                    count = 0
                #keeep curr char for next subarry grp 
                #form subarry with those chars in count
                #which are already even
                else:
                    count = 1
            
            else:
                count+=1
            i+=1
        return ans
                

            
        return ans
        

        