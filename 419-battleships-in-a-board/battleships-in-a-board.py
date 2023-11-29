class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        vis  = set()
        m,n  = len(board), len(board[0])
        def dfs(i,j):

            

            if ((i,j)  in vis )or  i<0 or j<0 or i>=m or j>=n or board[i][j]==".":

                return 
            vis.add((i,j))

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1, j)
            dfs(i,j-1)


        cnt= 0
        for i in range(m):
            for j in range( n):
                if board[i][j] =="X" and (i,j) not in vis: 
                    cnt+=1
                    dfs(i,j)
   
        return cnt

