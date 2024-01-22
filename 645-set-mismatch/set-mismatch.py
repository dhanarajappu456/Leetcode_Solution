'''
math solution 

we find ans1 -> which missin_num - dup_num  ----------eqn(1)
to find the miss and dup we need another equation 

so we find ans2 = miss^2-dup^2, from which we can get equation  ans3 = miss+dup-------eq(2) 


then it is easy to find miss and dup from these equation

t n 
s 1


'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans1 = 0
        ans2 = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            #m-d
            ans1 +=  i+1 - num
            #m^2 - d^2
            ans2 += (i+1)**2- num**2

        ans3 = ans2//ans1

        miss = (ans1+ans3)//2
        dup = miss-ans1
        return [dup,miss]
