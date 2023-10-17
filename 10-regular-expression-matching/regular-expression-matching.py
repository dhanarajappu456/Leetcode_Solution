class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        n,m  =  len(s),len(p)
        
        memo = [[-1 for j in range(len(p)+1)] for i in range(len(s)+1)]
        def rec(i,j):
            
            
            if j ==0:
                return i==0
            if i==0:
                for k in range(j+1):
                    if k%2!= 0:
                        if p[k]!="*":
                            return False
                        
                # # for example s=aa , p=aaaa, this must return False
                # return "*" in p[:j]
                return True
                        
                        
            if memo[i][j]!=-1:
                return memo[i][j]
            
            ans = False
            
            if p[j-1]=="." or s[i-1]==p[j-1]:
                ans =  rec(i-1,j-1)
            elif p[j-1]=="*":
                
                if s[i-1]==p[j-2] or p[j-2]==".":
                    #match or dont match(ignore char*)   
                    ans =  rec(i-1,j) or rec(i,j-2)
                else:
                    #don't match
                    ans  =  rec(i,j-2)

              

            memo[i][j] = ans
            return memo[i][j]
            
        return rec(n,m)