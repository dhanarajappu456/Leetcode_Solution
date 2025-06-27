class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n  = len(s)
        cnt  = 0 
        num = 0
        i = 0 
        while(i<n and num<=k):
            
            if s[n-1-i] =="1":
                if (num + 2**i )>k:
                    break
                else:
                    num = num+(2**i)
                    #print(i, s[n-1-i])
            
            cnt+=1
            
            i+=1
        print(cnt,i)
        while(i<n):
           
            if s[n-1-i] =="0":
                cnt+=1
            i+=1      
        return cnt      
        