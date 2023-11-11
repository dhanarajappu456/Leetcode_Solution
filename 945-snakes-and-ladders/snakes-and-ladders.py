

# [[-1, -1, -1, 8, 3, -1, 6, 56], [-1, -1, -1, -1, -1, -1, 2, -1], [-1, -1, -1, 33, 56, -1, 57, 21], [11, -1, -1, -1, 49, 36, -1, 48], [-1, -1, 11, -1, 14, 23, 56, 57], [-1, -1, 26, -1, -1, 38, -1, -1], [51, -1, -1, 63, -1, 31, 21, -1], [-1, -1, -1, 46, 47, -1, -1, -1]]



'''
the solution is to apply bfs

but remember, what you have to put in vis

since the same cell can be reached either directly with a dice roll or through a ladder or snake,  it is also said we cant perform more than 1 ladder or snake operation in a move, we cant add the cell to vis , just becuase we reached it.
as the summary ,  we need to add a cell ,  to vis if we reached it directly with dice roll , 

but no matter what , when we succesfully reach a cell, either via a jump or directly, we need to always add it to queue for processing next 

eg : 

# [[-1, -1, -1, 8, 3, -1, 6, 56], 
   [-1, -1, -1, -1, -1, -1, 2, -1], 
   [-1, -1, -1, 33, 56, -1, 57, 21], 
   [11, -1, -1, -1, 49, 36, -1, 48], 
   [-1, -1, 11, -1, 14, 23, 56, 57], 
   [-1, -1, 26, -1, -1, 38, -1, -1], 
   [51, -1, -1, 63, -1, 31, 21, -1], 
   [-1, -1, -1, 46, 47, -1, -1, -1]]


   in this when  we reach 4th cell in the second move   , we jump to 8  , and we cant jump to 56(from cell 8 ) as only 1 jump or drop is allowed per move , since cell 4 reached directly , we add it to vis . But ,  if we had also  added cell 8 to vis , then  from cell 2 in the second move we could have reached 8 directly  , and went to 56 , but since 8 is visited, this would have not been possible, so be careful 
   what u add to visit 
'''
from collections import deque as deq 
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        q = deq([])
        vis  =set()
        n = len(board)
        #flip the board horizontally
        board = board[::-1]
        def cellConvert(num):
            num = num -1 
            row  = (num)//n 
            col =  (num % n )
            if row % 2 ==1:
                col = n - 1 - (num % n )
            return (row, col)
        q.append((1,0))
        vis.add(1)

        while(q):
           
            num , move = q.popleft()
            a,b = cellConvert(num)
            if  num  ==  n**2:
                return move  if board[a][b]==-1 else -1 
            for i in range(num+1, min(n**2, num+6)+1):
       
                #check if direct cell possible form num are not already visited
                if i not in vis:
                    j,k  = cellConvert(i)
                    tar = board[j][k]
                    # cells that are reached with a jump , then just add to queue
                    if tar !=-1:
                        q.append((tar, move+1))
                    else:
                        q.append((i,move+1))
                    vis.add(i)
   
        return -1
        