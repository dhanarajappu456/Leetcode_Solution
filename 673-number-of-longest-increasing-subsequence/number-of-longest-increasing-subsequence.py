class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n= len(nums)
        dp =[1 for i in range(n)]
        cnt = [1 for i in range(n)]
  
        ind=0

        #FIND lenght of LIS
        max_ =1 
        while(ind<n):
            prevInd=ind-1
            while(prevInd>-1 ):
                if nums[prevInd]<nums[ind]:
                    if dp[prevInd]+1> dp[ind]:
                        dp[ind] =dp[prevInd]+1
                        cnt[ind] = cnt[prevInd]
                    elif dp[prevInd]+1== dp[ind]:
                        cnt[ind]+= cnt[prevInd]



                prevInd-=1
            max_ = max(max_, dp[ind])
            ind+=1
        ans  =0 
        print(dp, cnt)
        for i in range(n):
            if dp[i] == max_:
                ans+= cnt[i]
        return ans



