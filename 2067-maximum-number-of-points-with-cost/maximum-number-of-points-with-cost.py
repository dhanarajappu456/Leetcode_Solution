class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        m,n = len(points) , len(points[0])
        
        #store the max ans for all the cols for current row 
        curr  = [0 for j  in range(n)]
        #store the max ans for all cols for prev row 
        prev = [0 for j  in range(n)]
        
        #starting from last row we build the ans, such that each cell ans[r][c] 
        #(in reality we dont new to stroe enttire matrix ans , but  just need curr array where  create answers for current row ) , which stores the max value if we choose that particulat cell points[r][c]
        
        
        left,right = [0 for j  in range(n)] , [0 for j  in range(n)]
        for r in range(m-1,-1,-1):
            
            left[0] = prev[0]
            right[n-1] =   prev[n-1]
            for c in range(1,n):
                
                left[c] = max(prev[c],  left[c-1] -1)
            
            for c in range(n-2,-1,-1):
                
                right[c] =    max(prev[c] ,  right[c+1] -1)
                
                
                
            
            for c in range(n):
                
               
                    curr[c] = points[r][c]+ max(left[c],  right[c]) 
            
            prev = curr[:]
                    
                
        
          
        
        '''
            t m*n*n
            s n 
            
        '''
        return max(curr)
                
                
        