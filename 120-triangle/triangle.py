class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n =  len(triangle)
        
        prev  =[  0 for i  in range(n)] 
    
        for i in range(n-1,-1,-1):
            curr  =  [0  for i in range(n)]
            for j in range(i+1):
                
                if i == n-1:
                    curr[j] = triangle[i][j]

                else:
                    curr[j]  = min(prev[j] ,prev[j+1]) + triangle[i][j]
                            
            prev = curr 
        return prev[0]
        
        
   