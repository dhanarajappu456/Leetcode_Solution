class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        self.score = [0,0]
        @lru_cache(None)
        def rec(i,j,turn):
            
            if  i>j:
                #print(self.score[0],self.score[1])
                return self.score[0]>= self.score[1]


            
            self.score[turn]+=piles[i]
            
            if rec(i+1,j ,(turn+1)%2):
                return True


            self.score[turn]-=piles[i]

            self.score[turn]+=piles[j]
            if  rec(i,j-1,(turn+1)%2): return True

            self.score[turn]-=piles[j]

            return False
        
        n  = len(piles)
        return rec(0,n-1,0)


        