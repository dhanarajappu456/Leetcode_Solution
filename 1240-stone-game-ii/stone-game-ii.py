
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        #we focus to maximise alices points , given that both of them play optimallly
        #alice will  try out all the possibilites of choosing the 2m stones  and choose the max she could get, 
        #bob will try all the 2m possibilities and choose the path that make allice get the minimum point

        n = len(piles)
        memo  = {}
      

      # the state m,, ind , player indicate , at the index from ind to end , with first,  2m possibility of choosing the piles
      #if a particular player , plays , then what is the max codt alice can get 
        def rec(m,ind,player):    #timw m*ind*player = logn * n * 2 = 12*(10^4)*2 = 10^5
            
            if ind>=n:
                return 0
            
            if(m,ind, player ) in memo:
                return memo[(m,ind, player)]
            
       
            if player:
                
                
                points = 0
                piles_total = 0
                for i in range(2*m):
                    if ind+i< n:
                        piles_total += piles[ind+i]
                        points  = max(points, piles_total + rec(max(i+1,m), ind+i+1 , 0))
            
            else:
                points  = float("inf")
                for i in range(2*m):
                
                    points  = min(points , rec(max(i+1,m), ind+i+1 , 1))
                
            memo[(m,ind, player)] = points
            return  memo[(m,ind, player)]
        
        return rec(1,0,1)
        
                