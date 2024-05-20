'''
solution 2 - half number of subset sum  would have a particular position set if any mumber has a 1 at that 
position in nums, thus final ans
= 2**(n-1)*(2**i + 2**j+ 2**k ....), where i,j k etc... are some bits position set in any of the numbers 
= 2**(n-!)*(val) 
where we took val as the term 2**i +2**j + 2**k ....etc  , which is  ored values of all nums , 
which is nothing but a value  indicating the a bit position is set in any of the number .

'''

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ored  =0 
        n = len(nums)
        for num in nums:
            ored |= num
        return 2**(n-1)*ored

        