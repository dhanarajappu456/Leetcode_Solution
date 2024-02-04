from collections import defaultdict as dict , Counter as C
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        i=j=0
        n=len(s)
        mapS=dict(int )
        mapT=dict(int )
        mapT.update(C(t))
        res =float("inf")
        ansStr=""
        while(j<n):
            
            mapS[s[j]]+=1
            
            if not self.isValidWindow(mapS,mapT):
                j+=1
             
            else:
                while(self.isValidWindow(mapS,mapT)):
                    if j-i+1<=res :
                        res=j-i+1
                        ansStr=s[i:j+1]
                        
                    mapS[s[i]]-=1
                    if mapS[s[i]]==0:
                        mapS.pop(s[i])
                    i+=1                  
                j+=1
        return ansStr
    
    def isValidWindow(self,mapS,mapT):
        
        for i in mapT:
            if mapS[i]>=mapT[i]:
                continue
            return False
        return True
            
