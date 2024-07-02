class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        
        dp =[1,10]
        i=0
        for i in range(2,n+1):
            ans = dp[i-1]
            temp = i-1
            val= 9 
            cnt =1 
            while(temp):
                cnt*= val
                val-=1
                temp-=1
            cnt*=9
            ans+=cnt
            dp.append(ans )
        return dp[n]