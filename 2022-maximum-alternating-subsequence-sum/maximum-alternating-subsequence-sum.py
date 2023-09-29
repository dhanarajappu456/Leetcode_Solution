class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        the state of the dp is ind, pos , which is , max value at from ind to end , given that the next chosen value is at odd position if pos is 1 else at even position ,  if value is at even position 

        
        '''

        n=len(nums)

        memo = { }
        
    
        def rec(ind,pos):


            if ind ==n:
                return 0

            if (ind, pos ) in memo:
                return memo[(ind, pos)]
            

            tk = ( nums[ind] if pos ==0 else  -nums[ind])  + rec(ind+1,(pos+1)%2)
            not_  = rec(ind+1,pos)

            memo[(ind, pos)] =  max(tk, not_)
            return memo[(ind, pos)]


        return rec(0,0)