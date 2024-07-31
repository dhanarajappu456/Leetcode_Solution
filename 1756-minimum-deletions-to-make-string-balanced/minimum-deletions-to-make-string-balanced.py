class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n  = len(s)
        a_right ,b_left= 0 ,0
        #a_cnt initially is total number of 'a' in the array
        a_right  = s.count('a')
        ans  = float("inf")
        for i,c in enumerate(s):
            #dynamically get the number of a to right
            if c =='a':
                a_right-=1
            ans = min( ans , b_left+a_right)
            if c=="b":
                b_left+=1
        return ans

            