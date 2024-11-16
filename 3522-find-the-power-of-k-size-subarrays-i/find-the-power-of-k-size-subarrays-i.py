class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n   = len(nums)
        res  = []
        for i in range(n-k+1):
            prev = nums[i]-1
            ans = -1
            for j in range(i,i+k):
                if nums[j] == prev+1:
                    ans = max(ans, nums[j])
                    prev = ans
                else:
                    ans = -1
                    break        
            res.append(ans)
        return res