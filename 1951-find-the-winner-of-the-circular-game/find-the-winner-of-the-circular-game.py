class Solution:
    def findTheWinner(self, n: int, k: int) -> int:


        nums = [i+1 for i in range(n)]
        ind = 0


        while(len(nums)>1):

            ind  = (ind + k-1 )%len(nums)
            
            if ind == len(nums)-1:
                temp =  0
            else:
                temp   =ind
            val = nums.pop(ind)
            ind = temp
        
        return nums[0]
        