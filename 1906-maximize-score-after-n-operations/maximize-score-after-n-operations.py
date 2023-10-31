

'''

bruteforce memoisation  - using bitmask
we can choose any pair of number at any instant and calculate the gcd, 
at step1 we can make n^2 pair to calulate the step * gcd(nums[j]*nums[k ])
and then we can choose to make pairs in next step, with remaining numbers, 

but the step and same set of remaining numbers be repeated again and again ,which we can cache
the state (i,mask ) -> store max ans, when we are at ith step and mask denote remaining 
set of numbers we have in the nums array



'''
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        n = len(nums)
        mask  = (1<<n)-1
        memo ={}
        def rec(i,mask):
          
            if mask ==0:
                return  0
            if (i,mask) in memo :
                return memo[(i,mask)]
            ans = 0 
            for j in range(n-1): 
                if ((1<<(n-1-j))&mask)!=0:
                    for k in range(j+1,n):
                        if ((1<<(n-1-k))&mask)!=0:
                            newMask = mask&~(1<<(n-1-j))
                            newMask = newMask&~(1<<(n-1-k))
                            ans  = max(ans, i*math.gcd(nums[j],nums[k])+ rec(i+1, newMask))
            memo[(i,mask)] = ans 
            return ans 
        return rec(1,mask)
'''
n = len(nums)

t n*masK *(n^2) = n*(2^n)*n^2  = 14* 2^14  * 14 ^2 = 10^7, range of i , mask , and inner loop 
s  n*(2^n) +  aux
'''