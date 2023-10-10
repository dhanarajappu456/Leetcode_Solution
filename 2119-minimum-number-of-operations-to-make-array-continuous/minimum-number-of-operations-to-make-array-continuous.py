class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #sliding window
        
        '''
        we sort the array (of unique eleements )

        then starting at each index we find longest continous array(values from nums[l] .... nums[l]+n-1)
        then remaning  elments (n-windowlength) need to be changed to fit into this window.

        minimum among all of them is taken at the end 
        '''
        
        
        #to get only unique elements
        n =len(nums)
        nums = sorted(set(nums))  #nlogn
        r=0 
        ans  = n
        for l in range(len(nums)): #o(n)
            end = nums[l]+n-1
            while(r<len(nums) and nums[r]<=end): 
                r+=1
            windowLen  = r-1-l+1
            ans = min(ans,n - windowLen)
        return ans
     

     #t nlogn
     #s n (set)
        