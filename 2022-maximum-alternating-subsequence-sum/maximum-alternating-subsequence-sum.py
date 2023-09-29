class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        the state of the dp is ind, pos , which is , max value at from ind to end , given that the next chosen value is at odd position if pos is 1 else at even position ,  if value is at even position 


        T  n*2
        S  stk space (n) + memo (2*n)

        '''

        n=len(nums)

        # memo = { }
        
    
        # def rec(ind,pos):


        #     if ind ==n:
        #         return 0

        #     if (ind, pos ) in memo:
        #         return memo[(ind, pos)]
            

        #     tk = ( nums[ind] if pos ==0 else  -nums[ind])  + rec(ind+1,(pos+1)%2)
        #     not_  = rec(ind+1,pos)

        #     memo[(ind, pos)] =  max(tk, not_)
        #     return memo[(ind, pos)]


        # return rec(0,0)


        n = len(nums)
        dp = [[0 for i in range(2)] for j in range(n+1)]

        for ind in range(n-1, -1, - 1):
            for pos in range(2):
                tk = ( nums[ind] if pos ==0 else  -nums[ind])  
                tk += dp[ind+1][(pos+1)%2]
                not_  = dp[ind+1][pos]
                dp[ind][pos] =  max(tk, not_)
        return dp[0][0]


           

