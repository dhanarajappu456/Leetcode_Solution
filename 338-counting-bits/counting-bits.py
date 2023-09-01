class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp  =[0 for i in range(n+1)]
        
        for num in range(1,n+1):
            
            dp[num] = dp[num//2]+ (1 if num%2!= 0 else 0 )
        
        return dp
            
        