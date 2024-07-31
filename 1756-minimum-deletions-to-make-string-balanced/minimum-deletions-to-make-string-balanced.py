class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n  = len(s)
        a_count = [0 for i in range(n)]
        a_cnt =  0 
        for i in range(n-1,-1,-1):
           
            a_count[i] = a_cnt
            if s[i] == "a":
                a_cnt+=1
        b_left = 0 
        ans  = float("inf")
        for i,c in enumerate(s):
            a_right = a_count[i]
            ans = min( ans , b_left+a_right)
            if c=="b":
                b_left+=1
            
        return ans

            