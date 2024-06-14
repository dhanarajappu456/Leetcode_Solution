class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        ans =0
        nums.sort()
        mx = nums[0]
        print(nums)
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                print(nums[i],mx+1, abs(nums[i]-mx+1))
                ans+=abs(nums[i]-(mx+1))
                nums[i] = mx+1
            mx = nums[i]
        print(nums)
        return ans

        