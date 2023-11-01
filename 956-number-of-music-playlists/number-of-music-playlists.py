class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        MOD  = 10**9+7
        @lru_cache(None)
        def rec(totChosen, totUniqueChosen):

            
            if totChosen == goal:
                return 1 if totUniqueChosen ==n else 0 

            ans = 0 
            remainingUniqueSongs = n - totUniqueChosen
            #limiting the -ve values to 0 
            repeatableSongs  =  max(0,totUniqueChosen- k)
            ans +=  remainingUniqueSongs * rec(totChosen+1, totUniqueChosen+1)
            ans +=  repeatableSongs * rec(totChosen+1, totUniqueChosen)

            return ans
        return rec(0, 0 )%MOD

        '''
        brute- 
        t: 2^goal
        s : aux(goal)


        memoised  
        t goal*n  = 100*100 = 10^4
        s: goal*n +  aux 


        '''
        