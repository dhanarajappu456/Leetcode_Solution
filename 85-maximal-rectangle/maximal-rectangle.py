class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:


    
       
        ans = 0 
        m,n   =len(matrix), len(matrix[0])
        # maxArea = float("-inf")
        # for i in range(len(heights)):
        #     index = i
        #     while(stk and stk[-1][1]>=heights[i]):
        #         index,height = stk.pop()
        #         width = i-index
        #         area =  width * height
        #         maxArea =max(maxArea , area)
        #     stk.append((index,heights[i]))
        # return maxArea
        '''
        ["0","1","1","0","1"],
        ["1","1","0","1","0"],
        ["0","1","1","1","0"],
        ["1","1","1","1","0"],
        ["1","1","1","1","1"],
        ["0","0","0","0","0"]]
        '''

        heights =[0   for j in range(n) ]
      
        def helper(heights):
            print(heights)
            max_area  = 0 
            stk = [(-1,-1)]
            for j in range(n):
                ind = j
                print(stk)
                while(stk and stk[-1][1]>= heights[j]):
                    #3,5,10, 1 , we should nto misse the rectangle formed by 3 towards right , when inserting 1 
                    ind, height   = stk.pop()
                    area  = height *(j-ind)
                    max_area = max(area, max_area)
                width = (j-ind+1)
                area = width*heights[j]
                print("ar",area,j,ind)
                max_area =max(area, max_area)

                stk.append([ind, heights[j]])
            print('lo',max_area )
            
            for i in range(1,len(stk)):
                print("m",max_area)
                max_area  =max(max_area, (n - stk[i][0])*stk[i][1] )
                
            return max_area
        
        for i in range(m):
            #creating the heights array
            for j in range(n):

                if matrix[i][j] =="1":
                    heights[j] +=1
                else:
                    heights[j] = 0
          
            ans = max(ans , helper(heights))
        
            
        return ans





        