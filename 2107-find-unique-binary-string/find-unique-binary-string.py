class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        n  = len(nums)
        ans = ["" for i in  range(n)]
        pos = 0 
        for i,num in enumerate(nums):
            if num[i] == "0":
                ans[i] ="1"
            else:
                ans[i] ="0"
        return "".join(ans)

        