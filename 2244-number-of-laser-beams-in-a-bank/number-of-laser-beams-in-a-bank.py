class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prev  = 0 
        n = len(bank)
        ans = 0 
        for i in range(n):
            curr =0 
            val = bank[i]
            for j in range(len(val)):
                if val[j]=='1': 
                    curr+=1
            if curr!=0:
                
                ans += prev*curr
                prev = curr
        return ans 
        