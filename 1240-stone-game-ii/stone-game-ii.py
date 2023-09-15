

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        memo  = {}
      
        def rec(m,ind,alice):
            
            if ind>=n:
                return 0
            
            if(m,ind, alice ) in memo:
                return memo[(m,ind, alice)]
            
       
            if alice:
                
                
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
                
            memo[(m,ind, alice)] = points
            return  memo[(m,ind, alice)]
        
        return rec(1,0,1)
                
                
                
        