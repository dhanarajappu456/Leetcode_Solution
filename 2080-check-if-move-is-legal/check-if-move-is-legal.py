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
      
                    if board[x][y]==".":
                        break
                    elif board[x][y]!= color:
                        cnt+=1
                    else:
                        if cnt>=1 :
                            return True 
                        else:
                            break
                       
                        
            return False
            
        if helper():
            return True
        return False





        