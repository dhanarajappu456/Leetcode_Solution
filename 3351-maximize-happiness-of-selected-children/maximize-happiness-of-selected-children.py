class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n = len(happiness)
        ans  = 0
        for i in range(1,k+1):

            ans+= max(0,  happiness[n-i] - (i-1))

        return ans
        