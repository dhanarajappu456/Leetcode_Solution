class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        #infact we need  not have to have the 2d state, 

        '''
        as we are asked to find the condition of who wins, 
        we find the max difference from the perspective of the current player 
        the idea  is brute for all possibility 

        and the state i -> indicate  the max difference  out of all three possibility of choosing  the  elemeents , you can get for the current player 
        this player returns this max diff, and then next player calculate max diff for him/her, using this max diff
        
        '''
        piles = stoneValue

        n = len(piles)
        
        @lru_cache(None)
        def rec(i):

            if i >=n :
                return 0 
            ans = -float("inf")
            ans = max( ans, piles[i] -rec(i+1)) 
            
            if i+1<n:
                ans = max(ans, piles[i] + piles[i+1] - rec(i+2)) 
            if i+2<n :

                ans  = max(ans, piles[i] + piles[i+1]+ piles[i+2]- rec(i+3))
            return ans 
        aliceMaxDiff = rec(0)
        if aliceMaxDiff ==0:
            return "Tie"
        elif aliceMaxDiff >0 :
            return "Alice"
        else : 
            return "Bob" 

        