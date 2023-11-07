class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ''' the point to note is a group of o's with atleast one o at the edge , is uncapturable, so 
        try to find uncapturble grp and then mark all the rest as x
        '''
        m,n  = len(board), len(board[0])
        
        def out(i,j):
            return i<0 or j<0 or i>=m or j>=n
        
        def dfs(i,j):
            
            if out(i,j) or  board[i][j]!="O":
                return 
            
            board[i][j]="T"
            
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
      
        for i in range(m):

            
            
                if board[i][0] ==  "O":

                     dfs(i,0)
                if board[i][n-1] ==  "O":

                    dfs(i,n-1)
            
        for i in range(n):
            if board[0][i] ==  "O":

                dfs(0,i)
            if board[m-1][i] == "O":
  
                dfs(m-1,i)
            
  
        for i in range(m):
            for j in range(n):

                if board[i][j] != "T":
                    board[i][j]="X"
                elif board[i][j] == "T":
                    board[i][j]="O"
        return board




        