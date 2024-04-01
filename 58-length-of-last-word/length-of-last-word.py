class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)
        ans,final_ans =  0,0
        j=0
        while(j<n):
            
            ans=0
            while(j<n and s[j]!=' '):
                ans+=1
                j+=1
            

            while(j<n and s[j]==" "):
                j+=1
        return ans
        