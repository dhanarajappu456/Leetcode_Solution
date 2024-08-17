class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        m,n = len(points) , len(points[0])
        
        #store the max ans for all the cols for current row 
        curr  = [0 for j  in range(n)]
        #store the max ans for all cols for prev row 
        prev = [0 for j  in range(n)]
        
       
        #this is used to time optimise the solution 1 - 
        #left[c] stores the maximum answer among   all values to the left of current column c, including value at curren col c , 
        #from the previous rows answer( that is row just belwo, as we start from last row to first)
        #similarly right stores the max among values to the right columns inclusing current col c 
        left,right = [0 for j  in range(n)] , [0 for j  in range(n)]
        
        
        
         #starting from last row we build the ans, such that each cell ans[r][c] 
        #(in reality we dont new to stroe enttire matrix ans , but  just need curr array where  create answers for current row ) , which stores the max value if we choose that particulat cell points[r][c]
        
        for r in range(m-1,-1,-1):
            
            left[0] = prev[0]
            right[n-1] =   prev[n-1]
            #each left[c] stores max prev answer(taht is previosu visited row, that is row below )
            #from 0 to c(including c )
            for c in range(1,n):
                
                left[c] = max(prev[c],  left[c-1] -1)
            #each left[c] stores max prev answer(taht is previosu visited row, that is row below )
            #from n-1 to c(including c )
            for c in range(n-2,-1,-1):
                
                right[c] =    max(prev[c] ,  right[c+1] -1)
                
                
                
            #now to fill the answer for current row and cell 
            #we need to use which is the max among left and right for that column
            for c in range(n):
                
               
                    curr[c] = points[r][c]+ max(left[c],  right[c]) 
            
            #updating prev
            prev = curr[:]
                    
                
        
          
        
        '''
            t m*n*
            s n 
            
        '''
        return max(curr)
                
                
        