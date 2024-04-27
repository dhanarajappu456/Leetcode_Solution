'''
memoised solution 
t n^3
s n

'''
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:


        n = len(ring)
        m  = len(key)
        @lru_cache(None)
        #represnt the min steps neede to prcess key[j:] with i being current position in ring 
        def rec(i,j):

            if j == m:
              
                return 0
            
            ans  = float("inf")
            
            cnt = 0
            k=i
            while(cnt!=n):
                #when matching , check which direction gives the minimum , going clock or anticlock
                if ring[k]==key[j]:
                    ans  = min(ans,1+min(abs(i-k),abs(n-abs(i-k)))+rec(k,j+1))
                k+=1
                k= k% n
                cnt+=1
           
            return ans

        return rec(0,0)
