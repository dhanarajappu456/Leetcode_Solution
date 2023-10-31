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
