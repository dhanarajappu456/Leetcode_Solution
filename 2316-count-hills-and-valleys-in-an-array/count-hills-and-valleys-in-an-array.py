class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt  = 0
        n = len(nums)
        i = 0 
        while(i<n-1):
            j = i-1
            hill_l, hill_r ,  valley_l , valley_r = False, False , False, False
            while(j>=0 and nums[i] == nums[j]):
                j-=1
            
            if j>=0 :
                if nums[i]> nums[j]:
                    hill_l = True
                if nums[i]< nums[j]:
                    valley_l = True
            j = i+1
            while(j<n  and nums[i] == nums[j]):
                j+=1

            if j<n :
                if nums[i]> nums[j]:
                    hill_r = True
                if nums[i]< nums[j]:
                    valley_r = True
            
            if hill_l and  hill_r :
               
                cnt+=1
            if valley_l and valley_r:
               
                cnt+=1
            i = j
        return cnt 