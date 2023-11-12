'''
question asks for whether any direction have good line , with rmove, cmove,  as the end point 
'''

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        def helper():
         
            dir  =[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
            
            for d in dir:
                cnt = 0 
                x,y = rMove, cMove
                while(True):
                    x,y = x+d[0] , y+d[1]
                    if x<0  or  y<0 or x>=8 or  y>=8:
                        break
                    if (d[0],d[1]) ==(0,-1):
                            print(x,y)
                    #if the cell is empty cell , we can to further in current direction
                    if board[x][y]==".":
                        break
                    #if color is opposite of the given color, just increment the count 
                    elif board[x][y]!= color:
                        cnt+=1
                    #if the cell is same color as one end(given cell rMove and Cmove)
                    #then it  means,  we have a good line  ,  or we don't have , if there
                    #is not any opposite color of given "color"  in b/w
                    else:
                        if cnt>=1 :
                            return True 
                        else:
                            break
                       
                        
            return False
            
        if helper():
            return True
        return False





        