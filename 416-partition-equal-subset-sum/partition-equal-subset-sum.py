

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        
        # memo ={}
        # tot =sum(nums)
        # if tot%2 !=0 :
        #     return False
        # n = len(nums)
        # def rec(i, target):

            
            

        #     if i ==n:
        #         return target ==0
        #     if target ==0:
        #         return True
        #     if (i,target) in memo: 
        #         return memo[(i,target)]



        #     memo[(i, target)] = (rec(i+1, target - nums[i]) or rec(i+1, target))
            
        #     return memo[(i,target )]
        # return rec(0,tot/2)



        # tot =sum(nums)
        # if tot%2 !=0 :
        #     return False
        # n = len(nums)
        # # dp =[[True if t==0 else False for t in range(tot//2+1)  ] for i in range(n+1)]
        # dp[n][0] = True

        # n = len(nums)
        # for i in range(n-1,-1,-1):

        #     for tar in range(1,tot//2+1):
        #         ans = False
        #         if tar-nums[i]>=0:
        #             ans |=dp[i+1][tar-nums[i]]
                
        #         dp[i][tar] =  ans | dp[i+1][tar]
        # return dp[0][tot//2]

        tot =sum(nums)
        if tot%2 !=0 :
            return False
        n = len(nums)
        dp ={0}
        target =tot//2
        for i in range(n-1,-1,-1):
            nextDp =set()

            for tar in dp :
                if target==tar+nums[i]:
                    return True
                
                nextDp.add(tar+nums[i])
                nextDp.add(tar)
            dp = nextDp
        








        