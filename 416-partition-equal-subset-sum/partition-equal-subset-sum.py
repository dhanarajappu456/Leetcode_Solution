

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


        '''
        as wei iterate from back , we check if the current index can form target, with any of the subset sum obtained so far
        we store the all the possible , subset sum  found so far  in a set(as there can be duplicate)
        also note we might need only subset sum< target to be stored in to the set
        '''
        tot =sum(nums)
        if tot%2 !=0 :
            return False
        n = len(nums)
        #stores all possible subset sum from i+1 to end
        dp ={0}
        target =tot//2
        for i in range(n-1,-1,-1):#n

            nextDp =set()

            for tar in dp : #target
                if target==tar+nums[i]:
                    return True
                #we need to keep  sunbset sum which are less than target so, that we can 
                #form the target in future
                if tar+nums[i]<target:
                    nextDp.add(tar+nums[i])
                nextDp.add(tar)
            dp = nextDp
            '''
            t n*target
            s target(size of the dp ) since we only store sums that are less than target in the set,  the size is bounded by target

            '''
        

        








        