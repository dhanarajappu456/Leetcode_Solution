class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        mod= 10**9+7
        n = len(corridor)
        s=0
        ans = 1
        i= n-1
        s,p=0,0
        while(i>=0 ):
            
            
            while(i>=0 and s!=2):
                if corridor[i]=="S":
                    s+=1

                i-=1
            
            if i<0 and  s!=2: 
                return 0
            

            while(i>=0  and s==2):
                if corridor[i]=="P":
                    p+=1
                else:
                    break

                i-=1
  
            if i<0:
                p =0
            ans  *= (p+1)
       
            s,p =0,0


        
        

        return ans%mod

        