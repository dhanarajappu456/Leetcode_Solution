class Solution:


    def knightDialer(self, n: int) -> int:
        board =[[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]

        mod = 10**9+7    
        memo  ={}
        def invalidCell(i,j):
            return board[i][j]==-1

        def out_bound(i,j):

            return i<0 or j<0 or i>=a or j>=b 
        def rec(i,j,n):

            
            
            #we can't stand at any non numerical cell out of each of the n-1 movementd
            if invalidCell(i,j):
                return 0

            # if we reach this line this will be a valid cell (ie, it is numerical cell )
            if n==0 :
                  
                return 1
      


            #for all possbilities check

            if (i,j,n ) in memo:
                return memo[(i,j,n)]
            ans = 0 
            
            for d in dire:
         
                x,y =i,j
                valid_cell =True
                for m in d:

                    x += m[0] 
                    y += m[1]
                    
                    if (not out_bound(x,y)):
                      
                        continue
                    else:
                      
                        valid_cell =False
                        break
                if valid_cell:
                   
                    ans  = (ans%mod + rec(x,y,n-1)%mod)%mod
            memo[(i,j,n) ] = ans%mod
            return ans

            


                    

    


        #for each number as the starting number:
        dire  = [
            
            [(-1,0),(-1,0),(0,-1)],[(-1,0),(-1,0),(0,1)],
        [(0,1),(0,1),(-1,0)],[(0,1),(0,1),(1,0)],
        [(1,0),(1,0),(0,-1)],[(1,0),(1,0),(0,1)],
        [(0,-1),(0,-1),(-1,0)],[(0,-1),(0,-1),(1,0)]]
        a,b = 4,3
        ans= 0 
        for i in range(a):
            for j in range(b):

                if board[i][j] !=-1:
                   
                    ans  = (ans%mod + rec(i,j,n-1)%mod)%mod
                 

        return ans


           
            
            

            

        