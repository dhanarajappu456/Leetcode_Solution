class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num

     
        ans = 0
        n = len(nums)
        for poss  in  range((1<<n)):
            or_val  = 0 
            li  = []
           
            for i in range(n):
                if poss & (1<<i):
                    or_val|= nums[i]
                    li.append(nums[i])
       
            if or_val == max_or:
                ans+=1
        return ans


        '''
        time = 2**16 * 16  = (2**4)^4 * 16  = 10^4 * 10 = 10^5
        space = o(1)
        '''



        
        