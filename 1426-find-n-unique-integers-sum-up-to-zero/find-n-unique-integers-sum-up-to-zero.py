class Solution:
    def sumZero(self, n: int) -> List[int]:

      
        ans = [ ]
        val = 1
        while(n>1):
            
            ans.append(val)
            ans.append(-val)
            val+=1
            n-=2
        if n:
            ans.append(0)
        return ans



        