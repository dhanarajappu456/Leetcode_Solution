class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        ans = -1
        prev_min, prev_max= arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            ans  = max(ans, abs(prev_min - arr[-1]) , abs(prev_max  - arr[0]))
            prev_min, prev_max = min (prev_min, arr[0]) , max(prev_max, arr[-1])
        return ans

        