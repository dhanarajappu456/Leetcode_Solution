import bisect as bs 

'''
we store the LIS in the Lis array , length of which is LIS length so far
note the lis array may not be actual lis elements , but its length would be 
binary search  -to find the position in Lis array where the num cn be inserted
'''
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

        '''
        t nlogn 
        s n - at worst 

        '''

        
        
