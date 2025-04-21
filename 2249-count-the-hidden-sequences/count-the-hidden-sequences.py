class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        s = sum(differences)
        ans  = 0 
        n = len(differences)
        pref  = [0 for i in range(n)]
        prev =0
        for i in range(n):
            pref[i] = prev + differences[i]
            prev = pref[i]


        min_, max_ = min(pref) , max(pref)

        for num in range(lower ,upper+1):

            if lower <= (num + min_)  <= upper:
                
                if lower <= (num + max_)  <= upper:
                    
                    ans+=1

        
        return ans
