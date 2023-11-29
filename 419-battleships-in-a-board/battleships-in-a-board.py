'''
solution 1 
basically the a battle ship will be part of either part of continuous battleship along row or column not both

so , it is basically finding the number of these component  in the graph


t   mn
s   m + n(stack)

solution 2- o(1) space

we count the head of each battleship

that is   each battle ship head is characterised by the fact that ,


1:it is battle ship and
        and 
2: left of it  empty space(.) or no cell,  
         and 
2:  top of it empty space(.) or no cell




t mn
s 1

'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
       
        m,n  = len(board), len(board[0])
        cnt = 0 
        for i in range(m):
            for j in range( n):
                if board[i][j] =="X" and (j==0 or board[i][j-1]==".")  and (i==0 or board[i-1][j]=="."):
                    cnt+=1
             
   
        return cnt


