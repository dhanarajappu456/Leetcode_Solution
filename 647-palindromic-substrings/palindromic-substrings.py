class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt  = 0 
        for i in range(n):
            l,r  = i,i

            while(l>=0 and r<n):
                if s[l] == s[r]:

                    l-=1
                    r+=1
                    cnt+=1
                else:
                    break
            l,r=i,i+1

            while(l>=0 and r<n):
                if s[l] == s[r]:

                    l-=1
                    r+=1
                    cnt+=1
                else:
                    break


        return cnt
