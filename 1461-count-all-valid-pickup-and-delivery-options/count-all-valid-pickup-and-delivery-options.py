class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7

        '''

        for a prticular i  , we can place a pair of p and d at all empty spaces created by a specific permuation of 
        n-1

        ie, for a spceific n-1 ,permuation , we can have  2*(i-1)+1 spaces  , (remember , i is count of p or d )
        let this be "spaces"
        then we can have "spaces + spaces-1+ spaces-2 ....+1" as the current possibility for a particular permuation of i-1 , then total permuation  = tot prem of i-1 * curr permuations
    
        '''


        # Initialize the memoization table with 1 as the base case.
        memo = [1] * (n + 1)

        for i in range(2, n + 1):
            spaces =  2*(i-1)+1
            currPossibility = spaces*(spaces+1)//2
            
            prevPossibility  = memo[i-1]

            memo[i] = (prevPossibility*currPossibility) % MOD

        return memo[n]

        '''
        t n
        s n 

        '''


        
