class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        '''
        solution2- more short code  and single iteration on heights by helper than 
        approach of prev small and next small 
        we createdheights array which is height of building(represented by column with continuous  1s ), ending/base as 
        current row 
        for these heights we call the helper, which does return max rectagle in this as follows:

        1)the idea is if we had increading height we could have simply extended each building to right 
        and found the area of rectangles each of them with height of current element
        2) for a building of heights[j]  it cant be extended further to right , if we have a bulding at some 
        index to its right with height less than heights[j]. This observation leads to us that to chop the previous 
        greater heights heights[j] to this shorter height , so that all heights are increasing order.
        also while popping note that popped height could be extended to right(so we need to calculate area while 
        popping thes heights)till this j(excluding), where we have this shorter height.
        At end we assume  to extend remaining height to reight , where each rectangle formed so is of current height

        t m(n+n) = mn
        s n(heights)


        

        '''
    
       
        ans = 0 
        m,n   =len(matrix), len(matrix[0])
        heights =[0   for j in range(n) ]
        #helper to find max reactangle with current row as the base
        def helper(heights):
            max_area  = 0 
            stk = [(-1,-1)]
            for j in range(n):
                ind = j
                while(stk and stk[-1][1]>= heights[j]):
                    #3,5,10, 1 , we should nto misse the rectangle formed by 3 towards right , when inserting 1 
                    ind, height   = stk.pop()
                    area  = height *(j-ind)
                    max_area = max(area, max_area)
                width = (j-ind+1)
                #current height(heights[j])which is less than all popped value can fro rectangle with 
                #all popped values with a height of heights[j]
                area = width*heights[j]
                max_area =max(area, max_area)
                #assumed to have chopped all previosu greater heights to heights[j]
                #and inserted to stack with new position at ind
                stk.append([ind, heights[j]])
            #at the end , stack will be in increasing order
            #so , we need to calculate max rectangle at end as well
            for i in range(1,len(stk)):
                max_area  =max(max_area, (n - stk[i][0])*stk[i][1] )
            return max_area
        
        #for each  row finding max contnoud height with current row as base
        for i in range(m):
            #creating the heights array
            for j in range(n):
                if matrix[i][j] =="1":
                    heights[j] +=1
                else:
                    heights[j] = 0
          
            ans = max(ans , helper(heights))
        
            
        return ans





        