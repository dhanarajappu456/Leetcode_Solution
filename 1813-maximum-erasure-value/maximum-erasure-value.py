class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        

        n = len(nums)
        i,j  = 0,0
        set_ = set()
        sum_ = 0 
        ans = 0 
        while(j<n):
           
            while(nums[j] in set_):
                set_.remove(nums[i])
                sum_ -= nums[i]
                i+=1
            
            set_.add(nums[j])
            sum_+= nums[j]
            ans  = max(ans, sum_)
            j+=1
        return ans

