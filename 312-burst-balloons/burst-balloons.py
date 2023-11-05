class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def rec(i,j):


            if i>j:
                return 0
            ans = 0
            for p in range(i,j+1):
                ans  =  max(ans,  nums[i-1]*nums[p]*nums[j+1] + rec(i,p-1)+ rec(p+1,j))
            return ans
        nums = [1]+ nums+ [1]
        n = len(nums)
        return rec(1,n-2)

            
            

        