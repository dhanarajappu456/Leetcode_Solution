#approach 1
#naive approach , starting from all numbers from 0 to 2**n-1 we check whose bin representation  is   not in the list
#t 2**n
#s 1 

#approach 2 
# we try to create a number that differ from all the numbers in the list , 
# wrt to n position in the number 
# at the end we get a number that is not in the list
# t n 
# s 1


#approach 2
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        n  = len(nums)
        ans = ["" for i in  range(n)]
        pos = 0 
        for i,num in enumerate(nums):
            if num[i] == "0":
                ans[i] ="1"
            else:
                ans[i] ="0"
        return "".join(ans)

        