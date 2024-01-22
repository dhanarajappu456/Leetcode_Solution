class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans1 = 0
        ans2 = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            #m-d
            ans1 +=  i+1 - num
            #m^2 - d^2
            ans2 += (i+1)**2- num**2

        ans3 = ans2//ans1

        miss = (ans1+ans3)//2
        dup = miss-ans1
        return [dup,miss]
