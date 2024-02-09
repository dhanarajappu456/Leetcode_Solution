'''
LIS
T N^2
S N
'''


class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        hash_ = [-1 for i in range(n)]
        dp = [1 for ind in range(n)]
        res = []
        ind = 0
        while (ind < n):
            preInd = ind-1
            while (preInd > -1):
                if nums[ind] % nums[preInd] == 0:
                    if dp[ind]< dp[preInd] +1 : 
                        dp[ind] = dp[preInd] +1
                        hash_[ind] = preInd
                preInd -= 1
            ind += 1
        long = -1
        lastInd = -1
        for i in range(n):
            if long < dp[i]:
                long = dp[i]
                lastInd = i
        while (lastInd != -1):
            res.append(nums[lastInd])
            lastInd = hash_[lastInd]
        return res