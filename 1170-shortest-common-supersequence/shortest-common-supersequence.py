class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        @lru_cache(None)
        def rec(i,j) :


            if i == 0 or j == 0:
                return ""

            if str1[i-1] == str2[j-1]:
               
                return (rec(i-1, j-1) + str1[i-1])
            else:
                choice1 = rec(i-1, j)
                choice2 = rec(i, j-1)

                if len(choice1) <= len(choice2):
                    return choice2
                else:
                    return choice1

  

        
        m,n = len(str1),len(str2)
        lcs =  rec(m,n)
        i= 0 
        p1,p2 = 0,0
        ans = ""
     
        while(i<len(lcs)):
            
            while(p1<m and( lcs[i]!=str1[p1])):
                print("p1",str1[p1],p1,lcs[i],i)
                ans+=str1[p1]
                p1+=1

            while(p2<n and (lcs[i]!=str2[p2])):
                print("p2",str2[p2],p2,lcs[i],i)
                ans+=str2[p2]
                p2+=1
            
            ans+=lcs[i]
            p1+=1
            p2+=1
            i+=1
        return ans+str1[p1:] + str2[p2:]


                



                        
                       


                    

        