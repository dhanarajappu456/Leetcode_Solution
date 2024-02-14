class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

   
        res =[0 for i in range(len(nums))]
        posInd,negInd = 0,1
        for num in nums:
            if num>0:
                res[posInd] = num
                posInd+=2
            else:
                res[negInd] = num 
                negInd+=2
        return res

        