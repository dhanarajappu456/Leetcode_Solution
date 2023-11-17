#soltion is simple to get the optimal answer, we need to pair highest element with lowest and so on 
#so sort and apply 2 pointer
class Solution:
    def minPairSum(self, nums: List[int]) -> int:


        nums.sort() 

        n = len(nums)

        i,j  = 0,n-1
        ans = 0
        while(i<j):

            ans = max(ans, nums[i]+nums[j])
            i+=1
            j-=1       
        return ans