class NumArray:

    def __init__(self, nums: List[int]):
        self.pref  =[ 0 for i in range(len(nums))]
        self.pref[0]   = nums[0]
        n  = len(nums)
        self.nums = nums
        for i in range(1, n):

            self.pref[i] = self.pref[i-1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:

        return self.pref[right] - self.pref[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)