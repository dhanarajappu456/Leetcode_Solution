class Solution:
    def minimumLength(self, s: str) -> int:
    
        n = len(s)
        p1,p2 = 0,n-1


        while(p1<=p2):
           
            if s[p1] == s[p2]:
                c1 = s[p1]
                c2 = s[p2]
                while(p1<n and s[p1]==c1 ):
                    p1+=1

                while(p2>-1 and s[p2]==c2 ):
                    p2-=1
                if p1==p2 or len(s)==1:
                
                    return 1

            else:
                return p2-p1+1
        return 0
        