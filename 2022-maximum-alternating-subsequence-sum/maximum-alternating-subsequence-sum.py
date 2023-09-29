class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:


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