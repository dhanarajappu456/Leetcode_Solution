

# [[-1, -1, -1, 8, 3, -1, 6, 56], [-1, -1, -1, -1, -1, -1, 2, -1], [-1, -1, -1, 33, 56, -1, 57, 21], [11, -1, -1, -1, 49, 36, -1, 48], [-1, -1, 11, -1, 14, 23, 56, 57], [-1, -1, 26, -1, -1, 38, -1, -1], [51, -1, -1, 63, -1, 31, 21, -1], [-1, -1, -1, 46, 47, -1, -1, -1]]
from collections import deque as deq 
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        q = deq([])
        vis  =set()
        n = len(board)
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
       
                
                if i not in vis:
                    j,k  = cellConvert(i)
                    tar = board[j][k]
                    if tar !=-1:
                  
                        #ladder or snake target 
                            
                        q.append((tar, move+1))
                    else:

                        q.append((i,move+1))
                    vis.add(i)
   
        return -1
        