'''
#solution 2 - solution is same as the solution 1 
here we initally store all the sum of nums in ans variable then we have a aray indiacating the profit or loss 
if we xored each value in nums 

then we sort this array in descending order and take only profitable pair(that is sum of thier profit>0) into consideration
t nlogn
s n 

'''

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        ans = 0
        res =[0 for i in range(n)]
        for i,num in enumerate(nums):
            ans+= num
            res[i] = (num^k) -num
        res.sort(reverse =True)
 
        for i in range(0,n-1,2):
            profit_xor = res[i]+res[i+1]
            if profit_xor>0:
                ans+= profit_xor
        return ans 




        