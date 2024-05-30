class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost  = [ abs(ord(s[i] )- ord(t[i])) for i in range(len(s))]
        spent = 0 
        i,j  = 0,0
        ans =  0 
        while(j<n):
            spent+= cost[j]
            while(i<n and spent>maxCost):
                spent -= cost[i]
                i+=1
            ans  = max(ans, j-i+1)
            j+=1
        return ans




        return 0 
        