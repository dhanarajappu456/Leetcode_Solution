class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_ind  = 0 
        ans = -1
        for i in range(1,n ):
        
            ans = max(ans,values[i]+values[max_ind]+max_ind-i)
            if values[i]+(i- max_ind) >= values[max_ind]:
                max_ind = i
            
        return ans
