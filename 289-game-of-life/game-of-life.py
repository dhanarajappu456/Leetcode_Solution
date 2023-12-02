import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        m,n = len(board), len(board[0])

        def out(i,j):

            return i< 0 or j< 0 or i>=m or j>=n
            
        def neib_counter(i,j):

            dir =  [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
            cnt =0
            for d in dir:
                x , y = i+d[0], j+d[1]
                if not out( x, y):
                    if board[x][y] in [1,3]:
                        cnt+=1
            return cnt


    
        for i in range(m): 
            for j in range(n):
                neibs =neib_counter(i,j)
            
   
                if  board[i][j] ==1:
                    
                    if neibs <2 or neibs>3:
                  
                        board[i][j] = 1
                    else:

                        board[i][j] = 3
                        

                    
                elif board[i][j]== 0:
                    if neibs == 3: 
                        board[i][j] = 2
                    else:
                        board[i][j] == 0

        for i in range(m):
            for j in range(n):
                if board[i][j]  in [0,1]:
                    board[i][j] = 0
                else:
                    board[i][j]=1
              


                        
        