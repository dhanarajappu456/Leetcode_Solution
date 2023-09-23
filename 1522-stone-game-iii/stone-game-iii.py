class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        #we focus to maximise alices points , given that both of them play optimallly
        #alice will  try out all the possibilites of choosing 3 possibiliies  and choose the max she could get, 
        #bob will try all the 3  possibilities and choose the path that make allice get the minimum point

        piles = stoneValue
        n = len(piles)
        memo  = {}
      

      
        def rec(ind,player):   
            if ind>=n:
                return 0
            if(ind, player ) in memo:
                return memo[(ind, player)]
            if player:
                points =  -float("inf")
                piles_total =0
                for i in range(3):
                    if ind+i< n:
                        piles_total += piles[ind+i]
                        points  = max(points, piles_total + rec(ind+i+1 , 0))
            else:
                points  = float("inf")
                for i in range(3):
                    points  = min(points , rec(ind+i+1 , 1))
            memo[(ind, player)] = points
            return  memo[(ind, player)]
        
        aliceScore   = rec(0,1)
        bobScore  = sum(piles)- aliceScore

        if aliceScore == bobScore :
            return "Tie"
        elif aliceScore > bobScore:
            return "Alice"
        return "Bob"     
        