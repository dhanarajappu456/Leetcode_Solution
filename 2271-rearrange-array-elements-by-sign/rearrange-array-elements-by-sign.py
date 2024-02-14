'''
2pointer 

keep two pointer for pos and negative number position in the result array
then add the values to the res array as we iterate over the nums array 
t n 
s n (aux space  =res )

'''


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

        