class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        #infact we need  not have to have the 2d state, 

        '''

        we brute force , each player selecting the possible piles 
        ans 
        as we are asked to find the condition of who wins, 
        we find the max difference from the perspective of the current player , and return it , 

        ie,  the state i -> indicate  the max difference  out of all three possibility of choosing  the  elements , you can get for the current player 
        this player returns this max diff, and then next player calculate max diff for him/her, using this max diff
        
        '''
        piles = stoneValue

        n = len(piles)
        
        @lru_cache(None)
        def rec(i):

            if i >=n :
                return 0 
            maxDiff = -float("inf")
            maxDiff = max( maxDiff, piles[i] -rec(i+1)) 
            
            if i+1<n:
                maxDiff = max(maxDiff, piles[i] + piles[i+1] - rec(i+2)) 
            if i+2<n :
                maxDiff  = max(maxDiff, piles[i] + piles[i+1]+ piles[i+2]- rec(i+3))
            return maxDiff 
        aliceMaxDiff = rec(0)
        if aliceMaxDiff ==0:
            return "Tie"
        elif aliceMaxDiff >0 :
            return "Alice"
        else : 
            return "Bob" 

        