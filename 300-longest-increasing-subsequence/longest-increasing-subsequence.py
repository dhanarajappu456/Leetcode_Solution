import bisect as bs 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        Lis  = []
        ans = 0 
        for i ,num in enumerate(nums):
            ind = bs.bisect_left(Lis,num)
            if ind <len(Lis):
                Lis[ind] = num
            else:
                Lis.append(num)
            ans = max(ans, len(Lis))
        return ans 

        
        
