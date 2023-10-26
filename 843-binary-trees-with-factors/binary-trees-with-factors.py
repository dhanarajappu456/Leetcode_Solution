class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        '''
        choose each number as root and see which are the numbers factors of it present in the array and proceed recursion 
        also cache the result 
        memo[num] -> number of bin trees possible for num
        '''
        mod = 10**9+ 7
        memo =  { }
        numSet = { num for num in arr}
        def rec(num ):
         
            if num  in memo:
                return memo[num]

            l,r = 0,0 
            ans = 0
            for number in arr:
              

                if (num%number == 0 )and( num//number in numSet):
                      
                    l = rec(number)
                    r= rec(num//number) 
                    ans+= (l%mod)*(r%mod)%mod

            memo[num] = (1+ans)%mod
             
            return memo[num]
       
        ans=0 
        for root in arr: 
            ans =(ans + rec( root)%mod)%mod
    
        return ans

        