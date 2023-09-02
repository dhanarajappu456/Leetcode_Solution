class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:


        if k ==1 :
            return True
        n = len(nums)
        pref_sum = 0
        for i in range(n):

        
            nums[i] = nums[i] - pref_sum
            if nums[i]<0:
                return False
            
            pref_sum   += nums[i]
            
            if i>=(k-1):

                pref_sum -= nums[i-(k-1)]
        #print(nums) 
        return nums[-1]==0
        