class Solution:
    def stoneGame(self, piles: List[int]) -> bool:


        @lru_cache(None)
        def rec(i,j):


            if i>j:
                return 0

            if len(j-i+1)%2==0:

                return max(piles[i] + rec(i+1,j) ,  piles[j] + rec(i,j-1) )
            
            else:
                return max(  rec(i+1,j) ,  rec(i,j-1) )
        n = len(piles)
        return(0,n-1)




        