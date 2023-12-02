class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        q = deque(["X","O"])
        
        board = [["." for i in range(3)] for j in range(3)]
        tot_cell_filled =0 
        for m in moves: 
            pl = q[0]
            tot_cell_filled+=1
            q.append(q.popleft())



            r,c  = m[0],m[1]
            board[r][c] = pl

            count =0
            for i in range(3):
                if board[i][c] ==pl:
                    count+=1

            if count ==3: 
                return "A" if pl =="X" else "B"
            count  =0 
            for j  in range(3):
            
              
                if board[r][j] ==pl:
                    count+=1

            if count ==3: 
                return "A" if pl =="X" else "B"
            x,y  = 2,0
            count = 0
            if r+c == 2:
               
                while(x>=0 and y<3):
                    if board[x][y] ==pl: 
                        count+=1 
                    x-=1
                    y+=1

                if count ==3: 
                    return "A" if pl =="X" else "B"

            x,y  = 0,0  
            count = 0

            if abs(r-c) ==0 :
                while(x<3  and y<3):
                    if board[x][y] ==pl: 
                        count+=1 
                    x+=1
                    y+=1

                if count ==3: 
                    return "A" if pl =="X" else "B"
       
        return "Draw"   if tot_cell_filled==9 else "Pending"
            




        