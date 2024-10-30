class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans  = []
        n  = len(nums)
        nums.sort()
        k = n-1
        for k in range(n-1,1,-1 ): 
            #removing duplicate nums[k]
            #which gonna give same nums[i ] and nums[j]
            #if we choose same nums[k]
            #eg:[0,,0,,0,0]
            if k<n-1 and (nums[k] == nums[k+1]):
                continue
            
            j=k-1
            i=0
            while(i<j):

                if nums[i]+ nums[j]> (-nums[k]):
                    j-=1
                elif nums[i] + nums[j] < (-nums[k]):
                    i+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    #skipping same nums[i], nums[j] pair for 
                    # a particular value nums[k]
                    #eg: [-4,-4,4,-2-2-2,6]
                    while(i<j and nums[i]==nums[i+1]):
                        i+=1
                    i+=1
                    j-=1
            
        return ans